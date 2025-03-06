# nuke-macOS-caches

🧹 A simple Python script to completely remove all contents of the macOS Caches directory. Helps free up space and resolve potential issues caused by cached files.

## 🚀 Features
- Deletes all files and folders inside `~/Library/Caches`
- Automatically detects the user’s home directory
- Simple and lightweight, no dependencies required
- Safe execution with exception handling

## 📥 Installation
Clone the repository:  
```sh
git clone https://github.com/pedrorcruzz/nuke-macOS-caches.git
cd nuke-macOS-caches
```

## ▶️ Usage
Run the script using Python:  
```sh
make run
```

Alternatively, you can create an alias in your .zshrc for easier execution:

```sh
echo "alias ccache='pushd \"\$(pwd)\" > /dev/null && cd ~/your-path/nuke-macOS-caches && make run && clear && popd > /dev/null'" >> ~/.zshrc
source ~/.zshrc
ccache
```
You can also use a shell script to execute the command:

```sh
echo '#!/bin/bash
cd ~/your-path/nuke-macOS-caches
make run
sleep 1.3
clear' > ~/path/your-scripts/clear-cache.sh
```
```sh
chmod +x ~/path/your-scripts/clear-cache.sh
```

You can create alias in your zshrc for script:
```sh
echo "alias ccache='pushd \"\$(pwd)\" > /dev/null && cd ~/path/your-scripts && ./clear-cache.sh && popd > /dev/null'" >> ~/.zshrc
source ~/.zshrc
ccache
```


## ⚠️ Warning
This script **permanently deletes** all files in `~/Library/Caches`. Use it with caution.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
