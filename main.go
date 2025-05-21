package main

import (
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
)

func getSize(path string) (int64, error) {
	var totalSize int64 = 0

	info, err := os.Stat(path)
	if err != nil {
		return 0, err
	}

	if !info.IsDir() {
		return info.Size(), nil
	}

	err = filepath.WalkDir(path, func(_ string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}
		if !d.IsDir() {
			fi, err := d.Info()
			if err != nil {
				return err
			}
			totalSize += fi.Size()
		}
		return nil
	})

	return totalSize, err
}

func formatSize(size int64) string {
	units := []string{"B", "KB", "MB", "GB", "TB"}
	s := float64(size)
	var i int
	for i = 0; i < len(units); i++ {
		if s < 1024 {
			break
		}
		s /= 1024
	}
	if i >= len(units) {
		i = len(units) - 1
	}
	return fmt.Sprintf("%.2f %s", s, units[i])
}

func clearCache(ignoreGoBuild bool) (int64, error) {
	homeDir, err := os.UserHomeDir()
	if err != nil {
		return 0, err
	}
	cacheDir := filepath.Join(homeDir, "Library", "Caches")

	entries, err := os.ReadDir(cacheDir)
	if err != nil {
		return 0, err
	}

	var totalFreed int64 = 0

	for _, entry := range entries {
		if ignoreGoBuild && entry.Name() == "go-build" {
			continue
		}
		entryPath := filepath.Join(cacheDir, entry.Name())

		size, err := getSize(entryPath)
		if err != nil {
			fmt.Printf("Error getting size for %s: %v\n", entryPath, err)
			continue
		}

		err = os.RemoveAll(entryPath)
		if err != nil {
			fmt.Printf("Error deleting %s: %v\n", entryPath, err)
			continue
		}

		totalFreed += size
	}

	return totalFreed, nil
}

func main() {
	ignoreGoBuild := false

	freed, err := clearCache(ignoreGoBuild)
	if err != nil {
		fmt.Println("Error clearing cache:", err)
		return
	}

	fmt.Println("All contents of ~/Library/Caches have been deleted.")
	if ignoreGoBuild {
		fmt.Println("Note: 'go-build' folder was preserved.")
	}
	fmt.Println("Freed space:", formatSize(freed))
}
