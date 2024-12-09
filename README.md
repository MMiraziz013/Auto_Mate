Please Welcome Auto-Mate
=========

Auto-Mate is a Python desktop application that automates common tasks like email scheduling, countdown timers, screen recording, and YouTube video downloading. It uses a Tkinter-based graphical user interface and integrates with MySQL for email scheduling and status tracking.

Features
--------

*   Automated Email Scheduler: Schedule emails to be sent at a specific time.
    
*   Countdown Timer: Set and display countdown timers.
    
*   Screen Recorder: Record your screen for a specified duration (no audio).
    
*   YouTube Video Downloader: Download YouTube videos via link input.
    

Prerequisites
-------------

1.  Python 3.8 or newer (download from: [https://www.python.org/downloads/](https://www.python.org/downloads/))
    
2.  MySQL Workbench CE (download from: [https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/))
    
3.  Required Python Libraries (install via pip; see the "Dependencies" section below).
    

Installation and Setup
----------------------

1.  **Clone the Repository**
    
    *   ```bash
        git clone https://github.com/MMiraziz013/Auto_Mate.git
        
2.  **Install Dependencies**
    
    *   ```bash
        pip install -r requirements.txt
        
3.  **Set Up the Database**
    *   Install MySQL Workbench CE.
        
    *   Create a new database (e.g., auto\_mate\_db).
        
    ```sql

    CREATE TABLE your_table_name ( 
       id INT AUTO\_INCREMENT PRIMARY KEY,
       sender_email VARCHAR(255) NOT NULL, 
       sender_password VARCHAR(255) NOT NULL, 
       recipient_email VARCHAR(255) NOT NULL, 
       subject VARCHAR(255) NOT NULL, 
       message TEXT NOT NULL, 
       scheduled_time DATETIME NOT NULL, 
       status ENUM('pending', 'sent') DEFAULT 'pending'); 
    ``` 
4. **Update every occurrence of the table name in the code with your chosen table name.**

    ```python
    def get_db_connection(): 
        return mysql.connector.connect( 
            host="YOUR_HOST_NAME", 
            user="YOUR_MYSQL_USERNAME",
            password="YOUR_MYSQL_PASSWORD",
            database="YOUR_DATABASE_NAME" )
    ```
    
        
5. **Configure Gmail App Password**
    
    *   Log into your Gmail account.
        
    *   Navigate to "Google Account Settings" > "Security".
        
    *   Enable 2-Step Verification.
        
    *   Create an App Password for "Mail" and use it as the "Password" field in the email scheduler.
        
    *   For detailed instructions, visit: https://support.google.com/accounts/answer/185833?hl=en.
        

Running the Application
-----------------------

1.   ```
     python main.py
    
2.  Use the GUI to:
    
    *   Schedule an email.
        
    *   Set a countdown timer.
        
    *   Record your screen.
        
    *   Download YouTube videos.
        

Dependencies
------------

The application uses the following Python libraries:

*   mysql
    
*   mysql-connector-python
    
*   pyautogui
    
*   opencv-python
    
*   pytube
    
*   yt-dlp
    
*   ttkthemes
    
*   pyinstaller
    
*   tkcalendar
    
*   numpy
    

Install these dependencies with:

```
  pip install -r requirements.txt   
 ```
Packaging the Application into an Executable
--------------------------------------------

1.
    ``` 
     install pyinstaller
    ```
   
2. ```
    pyinstaller --onefile --windowed --icon=app_icon.ico main.py
    ```
3.  The .exe file will be created in the dist directory.
    

Adding an Icon to the Executable
--------------------------------

*   Replace app\_icon.ico in the command with the path to your icon file.
    
*   If no icon is specified, the default icon will be used.
    

Troubleshooting
---------------

*   MySQL Connection Issues: Verify credentials in the db\_utils.py file.
    
*   Email Sending Issues: Check the Gmail app password and ensure less-secure app access is enabled.
    
*   Library Installation Issues: Ensure the correct Python version and environment are being used.
    

References
----------

*   MySQL Documentation: [https://dev.mysql.com/doc/](https://dev.mysql.com/doc/)
    
*   pyautogui Documentation: [https://pyautogui.readthedocs.io/](https://pyautogui.readthedocs.io/)
    
*   OpenCV Documentation: https://docs.opencv.org/
    
*   pytube: [https://pytube.io/](https://pytube.io/)
    
*   yt-dlp Repository: [https://github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
    
*   Python Official Site: [https://www.python.org/](https://www.python.org/)

## License

**This project is licensed under the MIT License. See the LICENSE file for details.**

## Contributing
Contributions are welcome! Fork the repo, make your changes, and create a pull request.