THIS PROGRAM IS WINDOWS ONLY AND DEVELOPED FOR SMASH PLAYERS ON PC

To have this program work you need to:

1) Download "tesseract-ocr-setup-4.00.00dev.exe" from https://digi.bib.uni-mannheim.de/tesseract/
2) You must have installed Python 3.7.9
3) Change the file paths in AI.py to correspond with the file path you have for GSPStreamGrapher
4) Use pip to install pytesseract and pillow or any other Library (ex: import pytesseract) seen at the top of AI.py or LiveGraph.py  
	Example: pip install pillow
	Example: pip install pytesseract

To start the program:

1) Open terminal
2) Change directory to GSPStreamGrapher
3) Run the following command: python LiveGraph.py
4) Open separate terminal (you should now have a graph on one window and a terminal on the other)
5) Change directory to GSPStreamGrapher
6) Run the following command: python AI.py

To update GSP on graph
1) Select AI window (it should look like a grey game capture)
2) go to the character selection screen on online
3) Select character
4) press the tilda key (`)

The AI terminal should output a number and the graph should update

You should use window capture in Streamlabs to select the LiveGraph.py window 