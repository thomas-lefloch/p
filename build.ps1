rm main.exe
pyinstaller --onefile main.py --noconsole 
mv ./dist/main.exe ./main.exe