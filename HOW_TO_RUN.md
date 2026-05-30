# How to Run the Chatbot for Video Recording

## Step-by-Step Instructions

### Method 1: Using Command Prompt (CMD)

1. **Open Command Prompt**
   - Press `Windows + R`
   - Type `cmd` and press Enter

2. **Navigate to Project Directory**
   ```cmd
   cd C:\Users\DELL\Downloads\NLP Assignment
   ```

3. **Activate Virtual Environment**
   ```cmd
   venv\Scripts\activate
   ```
   
   You should see `(venv)` appear at the beginning of your command line.

4. **Run the Chatbot**
   ```cmd
   python src\chatbot.py
   ```

5. **Start Recording Your Video**
   - Use screen recording software (see recommendations below)
   - Start recording before running the chatbot
   - Or start recording after the chatbot loads

6. **Interact with the Chatbot**
   - Ask various questions (see sample queries below)
   - Show different confidence levels
   - Demonstrate successful and unsuccessful queries

7. **Exit the Chatbot**
   - Type `quit` or `exit` to close the chatbot
   - Stop your screen recording

### Method 2: Using PowerShell

1. **Open PowerShell**
   - Press `Windows + X`
   - Select "Windows PowerShell" or "Terminal"

2. **Navigate to Project Directory**
   ```powershell
   cd "C:\Users\DELL\Downloads\NLP Assignment"
   ```

3. **Activate Virtual Environment**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   If you get an error about execution policy, run:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Run the Chatbot**
   ```powershell
   python src\chatbot.py
   ```

## 🎬 Screen Recording Software Recommendations

### Free Options:
1. **OBS Studio** (Best for quality)
   - Download: https://obsproject.com/
   - Professional-grade, free and open source
   - Can record specific window or full screen

2. **Windows Game Bar** (Built-in)
   - Press `Windows + G` to open
   - Click record button
   - Simple and already installed

3. **ShareX** (Easy to use)
   - Download: https://getsharex.com/
   - Lightweight and feature-rich

4. **Bandicam** (Free version with watermark)
   - Download: https://www.bandicam.com/

### Paid Options:
- Camtasia
- Snagit
- Screencast-O-Matic

## 📝 Sample Queries for Demonstration

### Show High Confidence Matches:
```
1. "What are the admission requirements?"
2. "How do I apply for admission?"
3. "Is there a Computer Science program?"
4. "Are scholarships available?"
5. "What is the fee structure?"
```

### Show Paraphrasing Capability:
```
6. "How much does it cost?"
7. "When can I start?"
8. "Do you have CS program?"
9. "What if I fail a course?"
10. "Can international students get scholarships?"
```

### Show Medium Confidence:
```
11. "Tell me about fees"
12. "What about programs?"
```

### Show Fallback Response (Low Confidence):
```
13. "What's the weather like?"
14. "Can I get a refund?"
15. "Tell me about parking"
```

## 🎥 Video Recording Tips

### Before Recording:
1. Close unnecessary applications
2. Clear your desktop (optional)
3. Increase CMD/PowerShell font size for better visibility:
   - Right-click title bar → Properties → Font → Size 20 or larger
4. Test the chatbot once to ensure it works
5. Prepare your sample queries in a text file

### During Recording:
1. **Introduction (30 seconds)**
   - State your name and roll number
   - Briefly explain what you're demonstrating
   - Example: "Hi, I'm Naqcho Ali, CS-113. This is our NLP FAQ Chatbot for university admissions."

2. **Show Startup (30 seconds)**
   - Navigate to directory
   - Activate virtual environment
   - Run the chatbot
   - Show loading messages

3. **Demonstrate Queries (2-3 minutes)**
   - Ask 8-10 diverse questions
   - Point out similarity scores
   - Show high, medium, and low confidence examples
   - Demonstrate paraphrasing capability

4. **Show Fallback (30 seconds)**
   - Ask an out-of-domain question
   - Show the fallback response

5. **Conclusion (30 seconds)**
   - Exit the chatbot
   - Briefly summarize key features
   - Thank you message

### After Recording:
1. Review the video
2. Trim any unnecessary parts
3. Add title slide (optional)
4. Export in MP4 format
5. Keep video under 5 minutes

## 🎯 Recommended Video Structure (3-5 minutes)

```
00:00 - 00:30  Introduction
00:30 - 01:00  Starting the chatbot
01:00 - 03:30  Demonstrating queries
03:30 - 04:00  Showing fallback mechanism
04:00 - 04:30  Conclusion
```

## 📊 What to Highlight in Video

✅ **Show these features:**
- Chatbot loads FAQ dataset (18 entries)
- Sentence transformer model loads
- Interactive chat interface
- High confidence matches (similarity > 0.7)
- Medium confidence matches (0.5 - 0.7)
- Low confidence / fallback (< 0.5)
- Paraphrasing capability
- Matched FAQ question display
- Clean exit

## 🐛 Troubleshooting

### If chatbot doesn't start:
```cmd
# Make sure you're in the right directory
cd C:\Users\DELL\Downloads\NLP Assignment

# Make sure virtual environment is activated
venv\Scripts\activate

# Check if Python is accessible
python --version

# Try running again
python src\chatbot.py
```

### If you get "Module not found" error:
```cmd
# Reinstall dependencies
pip install -r requirements.txt
```

### If NLTK data is missing:
The chatbot will automatically download it on first run. Just wait for it to complete.

## 💡 Pro Tips

1. **Font Size**: Make CMD text large enough to read in video
   - Right-click CMD title bar → Properties → Font → Size 20+

2. **Window Size**: Maximize CMD window for better visibility

3. **Speak Clearly**: Narrate what you're doing (optional but recommended)

4. **Prepare Queries**: Have your test queries ready in a text file to copy-paste

5. **Show Variety**: Demonstrate different types of queries and confidence levels

6. **Keep it Short**: 3-5 minutes is ideal, don't exceed 7 minutes

7. **Test First**: Do a practice run before recording

## 📤 Uploading Your Video

### Options:
1. **YouTube** (Unlisted)
   - Upload as unlisted video
   - Share the link in your submission

2. **Google Drive**
   - Upload video
   - Set sharing to "Anyone with the link"
   - Share the link

3. **OneDrive / Dropbox**
   - Similar to Google Drive

4. **Direct Submission**
   - If file size is reasonable (<100MB)
   - Submit directly via LMS

## ✅ Final Checklist Before Recording

- [ ] Chatbot runs without errors
- [ ] Virtual environment is activated
- [ ] Screen recording software is ready
- [ ] Sample queries are prepared
- [ ] CMD font size is increased
- [ ] Desktop is clean (optional)
- [ ] You know what to say/demonstrate
- [ ] Video will be 3-5 minutes long

---

**Good luck with your recording! 🎬**

If you encounter any issues, refer to the README.md or REPORT.md for more details.
