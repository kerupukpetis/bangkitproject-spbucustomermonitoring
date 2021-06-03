# bangkitproject-spbucustomermonitoring
Program to Monitor plat number in SPBU. Include Machine learning program, program to send data to Firestore using python, and android application to read data form firestore.

The flow to run all programs on the Montirong gas station project.

//Android Application (Step 1 - 4, Step 10 - 13)
//Machine Learning (Step 5 - 9)
1. Install android app
2. Register for a gas station account to get an account key that will be used in the trial use of machine learning programs.
3. Save the account key. The account key in the form of a gas station code that is registered during account creation is applied.
4. Save your email address and password to log into the application later, to monitor from Firestore.
5. Save the image you want to test in a fixed and unchanging place. Images can use the sample images provided.
6. In running the machine learning program, first prepare the address where to save the photo file that you want to try.
7. Change the photo address in the 'load image' program, with the address that has been prepared.
8. Change the 'document' address in the write data program to Firestore, with the account key that you already have according to the previous step.
9. Run the application, then any machine learning reading results will be stored in Firestore.
10. Open the application and login using the email and password used during registration.
11. The application will automatically retrieve data from Firestore according to the address of the 'document' that has been created.
12. The application can monitor the results of the number plate reading and gasoline.
13. Data is displayed on the application dashboard in the form of list items and graphs.
