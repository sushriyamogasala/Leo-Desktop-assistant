This Machine Learning (ML) project allows you to control your entire PC using voice commands.

The application can execute various tasks based on the provided voice input:

- Automates YouTube
- Downloads YouTube videos
- Captures photos and videos
- Takes screenshots
- Plays your favorite music
- Adjusts volume and brightness
- Automates WhatsApp
- Controls Chrome
- Provides the current temperature
- Shows the current date, day, and time
- Gives daily news updates
- Displays your current location
- Tells jokes and interesting facts
- Shows PC battery status
- Opens C, D, E, and F drives
- Sets alarms
- Shuts down or restarts the PC
- Remembers and reminds notes
- Notifies our schedule
- Includes a security system with:
  - Face Recognition (for user verification)
  - Password (if face recognition fails)

After passing the security checks, users can issue commands to perform any of the listed tasks.

To set up face verification, follow these steps:

1. Run `sample_generator.py` to gather sample images for face verification, which will be saved in the samples folder.
2. Execute `Model_Trainer.py` to train these samples, creating a training file in the trainer folder.

To use the Leo program, do the following:

1. Install all required packages listed in `requirements.txt`.
2. Start the program by running `script.py`.
3. Activate the program by saying "hey Leo".
4. Verify your identity through face recognition or password, then issue your commands.
5. To deactivate, say "Sleep" or "you need a break" or "quit".
6. Reactivate the program anytime with "hey Leo".

For detailed input commands and password instructions, refer to the `exe()` and `security()` functions in `Leo.py`.
