# movingpics
python script that will create and move folders in the saved pictures 

'PICTURES_PATH' is the path on my machine that is located on a file called '.env' 
To make it run in the background (windows): 

Open the Task Scheduler by pressing the Windows key + R and typing "taskschd.msc".
1. Click on "Create Task" in the right-hand pane.
2. Give the task a name and description.
3. In the "Triggers" tab, set up the schedule for when you want the task to run.
4. In the "Actions" tab, click "New" and then "Start a program".
5. In the "Program/script" field, type "python.exe".
6. In the "Add arguments (optional)" field, specify the path to your python file, for example: "script.py".
7. Check the "Hidden" box in the "General" tab to run the task in the background.
8. Click "OK" to save the task.
