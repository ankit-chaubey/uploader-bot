# 📂 Uploader Bot 🚀

Welcome to the **Uploader Bot**! This Python-based bot is specifically designed for **content creators** 📸 who need to upload multiple files and thumbnails in bulk to Telegram 📱. It automates the process, saving you time and effort! 🎯

## 🌟 Key Features

- 🔄 **Auto-Zip**: Automatically compresses folders and their contents into `.zip` files.
- 📝 **Make**: Generates a `.txt` file that contains folder details for structured uploads.
- ⚡ **Uploader**: Uploads files and thumbnails in batches via Telegram Bot.
- 🔧 **Network Handling**: If the bot encounters network issues or crashes, it saves the progress and resumes from where it left off. No uploads are lost! 🔄
  
---

## 🛠️ Requirements

To get started, you'll need the following:

- 💻 **Python 3.7+**
- 📱 **Telegram API credentials** (API ID & Hash)
- 📦 **Pyrogram v2 library**
- 🔧 Additional Python libraries: `tqdm`, `colorama`, `decouple`

---

## 📥 Installation Steps

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ankit-chaubey/uploader-bot.git
cd uploader-bot
```
### 2️⃣ Install the required dependencies

Ensure you have Python 3.7+ installed, then install all the required libraries:
```
pip install -r requirements.txt
```

If you don't have a requirements.txt file, here’s what it should include for the new libraries:

```
pyrogram==2.x
tqdm
colorama
decouple
```
---

### 3️⃣ Set up Telegram API credentials

1. Visit Telegram's API Development Tools and log in with your phone number.

2. Create a new application to get your API ID and API Hash.

3. Add your credentials to config.py or set them as environment variables.

```
API_ID = 'your_api_id_here'
API_HASH = 'your_api_hash_here'
BOT_TOKEN = 'your_bot_token_here'
```

---

📝 Usage Instructions

Step 1: Run `autozip.py`

This script will automatically zip each folder and place the .zip file inside the respective folder.

```
python autozip.py
```

Step 2: Run `make.py`

This will generate a txt file for each folder, containing details of the files and thumbnails for easy batch uploading.

```
python make.py
```

Step 3: Run `uploader.py`

Finally, run the bot to upload your files and thumbnails in batches. The bot will also handle network issues, ensuring that uploads resume from where they left off in case of any interruptions.

```
python uploader.py
```

---

## 🌍 Handling Network Issues

The bot is designed to handle network interruptions. If there's a crash or disconnect, it saves the progress so uploads can continue from where they were interrupted. This ensures no data loss during the upload process! 🔄


---

## 🚧 Currently Private

This bot is private and not yet publicly available for everyone. However, if you really need it and think it would benefit you, feel free to contact me. I'll review your request and may provide access if I feel it's the right fit! 💌


---

#### 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details. 📜


---

### 🤝 Contributing

Contributions are welcome! If you have suggestions or would like to improve the bot, feel free to fork the repository and submit a pull request. Let's make this bot even better together! 💪


---

### 💬 Contact

For any questions or if you'd like to request access to the bot:

📧 Email: [Contact](mailto:m.ankitchaubey@gmail.com)

🔗 GitHub: [ankit-chaubey](https://github.com/ankit-chaubey)

---

Thank you for checking out the Uploader Bot! Happy uploading! 🚀🎉
