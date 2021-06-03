# bangkitproject-spbucustomermonitoring
Program to Monitor plat number in SPBU. Include Machine learning program, program to send data to Firestore using python, and android application to read data form firestore.

The flow to run all programs on the Montirong gas station project.

//Android Application (Step 1 - 4, Step 12 - 15)
//Machine Learning (Step 5 - 11)
1. Install android app
2. Register for a gas station account to get an account key that will be used in the trial use of machine learning programs.
3. Save the account key. The account key in the form of a gas station code that is registered during account creation is applied.
4. Save your email address and password to log into the application later, to monitor from Firestore.
5. Save the image you want to test in a fixed and unchanging place. Images can use the sample images provided.
6. Save the 'number plate' model and 'gasoline liter' model in a fixed and unchanging place.
7. In running the machine learning program, first prepare the address where to save the photo file that you want to try.
8. Change the photo address in the 'load image' program, with the address that has been prepared.
9. Replace the model address in the 'load model' program, with the model address 'number plate' on model1 and model address 'liter gasoline' on model2.
10. Change the name of the string data 'documents' in the variable 'users_ref', with the account key that you already have according to the previous step.
11. Run the program .py, then any machine learning reading results will be stored in Firestore.
12. Open the application and login using the email and password used during registration.
13. The application will automatically retrieve data from Firestore according to the address of the 'document' that has been created.
14. The application can monitor the results of the number plate reading and gasoline.
15. Data is displayed on the application dashboard in the form of list items and graphs.
