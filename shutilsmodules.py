import shutil
import os

"""
--- SHUTIL MODULE LOGIC (Advanced File Manager) ---

1. Core Purpose: Python's built-in high-level file operations manager. 
   It handles copying, moving, deleting fully populated directories, and creating zip archives.
   
2. Why use it over 'os'?: 
   The 'os' module is good for paths, but 'shutil' handles heavy lifting. 
   It copies metadata (permissions/time) and can delete folders that are NOT empty.

3. 'Family Call' App Use Cases:
   - Moving user profile pictures from a '/temp' scanning folder to the main '/media' folder.
   - Creating a compressed .zip file of a user's chat history for backup downloads.
"""

# ==========================================
# PRACTICAL SYNTAX FOR 'FAMILY CALL' BACKEND
# ==========================================

# Dummy files setup (just for understanding, don't run blindly)
# open("temp_profile.jpg", "w").close() 

# 1. COPY: Make an exact copy of a file (with metadata)
# Syntax: shutil.copy2(source, destination)
# shutil.copy2("temp_profile.jpg", "backup_profile.jpg")


# 2. MOVE (Cut & Paste): Move a file from temp to main folder
# Syntax: shutil.move(source, destination)
# shutil.move("temp_profile.jpg", "media/profile_pics/user_123.jpg")


# 3. DELETE ENTIRE FOLDER (Ruthless Delete like Linux 'rm -rf')
# Syntax: shutil.rmtree(folder_path)
# Warning: This deletes the folder even if it contains 1000 files!
# shutil.rmtree("old_chat_logs_folder")


# 4. ZIP BACKUP: Compress a folder into a .zip file for user download
# Syntax: shutil.make_archive(zip_name, format, folder_to_compress)
# shutil.make_archive("user_123_chat_backup", "zip", "media/chats/user_123")