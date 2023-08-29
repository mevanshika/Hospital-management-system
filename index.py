'''
------------------------------------------------------
Hospital Management System Project
Author: Vanshika Sharma
Roll No: 1
Sec: A
File: index.py
Version 0.9b
-----------------------------------------------------------
'''
import sys
import time
import os

from termcolor import cprint
import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet


def loading_screen():
    total_iterations = 10
    print("\033c", end="")
    print("Initializing...")
    for i in range(total_iterations):
        time.sleep(0.5)
        progress = (i + 1) * 10
        print("\033c", end="")
        print(f"[{'=' * i}{' ' * (total_iterations - i - 1)}] {progress}%")

    print("\033c", end="")
    print("Loading complete!")
    os.system('cls')

def exit_screen():
    total_iterations = 10
    print("\033c", end="")
    cprint("Attention! Too many attempt", "red", attrs=["bold"], file=sys.stderr)    
    for i in range(total_iterations):
        time.sleep(0.7)
        progress = (i + 1) * 20
        print("\033c", end="")
        print(f"[{'=' * i}{' ' * (total_iterations - i - 1)}] {progress}%")

    print("\033c", end="")  
    	
def AppointmentIndexInDoctorsDataBase (patient_ID) :
	for i in Doctors_DataBase :
		for j in Doctors_DataBase[i] :							
			if str(patient_ID) == str(j[0]) :
				Appointment_index = Doctors_DataBase[i].index(j)
				return Appointment_index,i
#loading_screen()	
print(" _______________________________________________________________________________________________________________________________________")
print("|                                                  || WELCOME TO ||                                                                     |")
print("|                        _ _        _                                                            _     __           _                   |")
print("|   /\  /\___  ___ _ __ (_) |_ __ _| |   /\/\   __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_  / _\_   _ ___| |_ ___ _ __ ___    |")           
print("|  / /_/ / _ \/ __| '_ \| | __/ _` | |  /    \ / _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __| \ \| | | / __| __/ _ \ '_ ` _ \   |")
print("| / __  / (_) \__ \ |_) | | || (_| | | / /\/\ \ (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_  _\ \ |_| \__ \ ||  __/ | | | | |  |")
print("| \/ /_/ \___/|___/ .__/|_|\__\__,_|_| \/    \/\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__| \__/\__, |___/\__\___|_| |_| |_|  |")
print("|                  |_|                                            |___/                                    |___/                        |")
print("|_______________________________________________________________________________________________________________________________________|")
	

tries = 0
tries_flag = ""
while tries_flag != "Close the program" :

		Patients_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()
		Doctors_DataBase  = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()
		print("\n")		
		cprint("-----------------------------------------", "magenta", attrs=["underline"], file=sys.stderr)
		cprint("|Administration (Enter 1)	        |\n|User mode (Enter 2)			|", "magenta", attrs=["blink"], file=sys.stderr)
		cprint("-----------------------------------------",  "magenta", attrs=["underline"], file=sys.stderr)
		cprint("\nEnter your choice", "magenta", attrs=["underline"], file=sys.stderr)
		Admin_user_mode = input(":=> ") 
		if Admin_user_mode == "1" :		
				os.system('cls')																	
				print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")
				cprint("Please enter your password : ", "magenta", attrs=["underline"], file=sys.stderr)
				Password = input(":=>  ")
				os.system('cls')
				while True :
					
					if Password == "admin" :
						cprint("-----------------------------------------", "red", attrs=["underline"], file=sys.stderr)
						cprint("|          (Main Menu)                  |", "red", attrs=["underline"], file=sys.stderr)
						cprint("-----------------------------------------", "red", attrs=["underline"], file=sys.stderr)
						cprint("|To Manage patients (Enter 1) 		|\n|To manage doctors (Enter 2)	 	|\n|To manage appointments (Enter 3) 	|\n|To Back (Enter E)			|", "red", attrs=["underline"], file=sys.stderr)
						cprint("-----------------------------------------", "red", attrs=["underline"], file=sys.stderr)
						cprint("\nEnter your choice", "magenta", attrs=["underline"], file=sys.stderr)
						AdminOptions = input (":=> ")
						AdminOptions = AdminOptions.upper()
						if AdminOptions == "1" :
								os.system('cls')															#Adminimstration 
								cprint("-----------------------------------------", "green", attrs=["bold"], file=sys.stderr)
								cprint("|          (Manage Patients)             |", "green", attrs=["bold"], file=sys.stderr)
								cprint("------------------------------------------", "green", attrs=["bold"], file=sys.stderr)
								cprint("|To add new patient (Enter 1)	  	 |", "green", attrs=["bold"], file=sys.stderr)
								cprint("|To display patient (Enter 2)	  	 |", "green", attrs=["bold"], file=sys.stderr)
								cprint("|To delete patient data (Enter 3)        |", "green", attrs=["bold"], file=sys.stderr)
								cprint("|To edit patient data (Enter 4)      	 |", "green", attrs=["bold"], file=sys.stderr)
								cprint("|To Main-Menu (Enter E)    1  		 |", "green", attrs=["bold"], file=sys.stderr)
								cprint("-----------------------------------------", "green", attrs=["bold"], file=sys.stderr)
								cprint("\nEnter your choice", "magenta", attrs=["underline"], file=sys.stderr)
								Admin_choice = input (":=> ")
								Admin_choice = Admin_choice.upper()
								loading_screen()
								if Admin_choice == "1" : 										
											try :		
												os.system('cls')
												cprint("-----------------------------------------\n|          (Add Patient Record)         |\n-----------------------------------------",  "green", attrs=["bold"], file=sys.stderr)
												patient_ID = int(input("Enter patient ID : "))
												while patient_ID in Patients_DataBase :		
													patient_ID = int(input("This ID is already in use, please try another ID : "))					
												Department=input("Enter patient department                : ")
												DoctorName=input("Enter name of doctor following the case : ")
												Name      =input("Enter patient name                      : ")
												Age       =input("Enter patient age                       : ")
												Gender    =input("Enter patient gender                    : ")
												Address   =input("Enter patient address                   : ")
												RoomNumber=input("Enter patient room number               : ")
												Patients_DataBase[patient_ID]=[Department,DoctorName,Name,Age,Gender,Address,RoomNumber]
												cprint("----------------------Patient details added successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
											except :
												print("Patient ID should be an Integer number")
										
								elif Admin_choice == "2" :						
											try :	
												os.system('cls')	
												cprint("-----------------------------------------\n|          (Search Patient Record)      |\n-----------------------------------------",  "green", attrs=["bold"], file=sys.stderr)												
												patient_ID = int(input("Enter patient ID : "))
												while patient_ID not in Patients_DataBase :
													patient_ID = int(input("Incorrect ID, Please Enter valid patient ID : "))
												print("\npatient name        : ",Patients_DataBase[patient_ID][2])
												print("patient age         : ",Patients_DataBase[patient_ID][3])
												print("patient gender      : ",Patients_DataBase[patient_ID][4])
												print("patient address     : ",Patients_DataBase[patient_ID][5])
												print("patient room number : ",Patients_DataBase[patient_ID][6])
												print("patient is in "+Patients_DataBase[patient_ID][0]+" department")
												print("patient is followed by doctor : "+Patients_DataBase[patient_ID][1])
											except :
												print("Patient ID should be an Integer number")
								
								elif Admin_choice == "3" :										
											try :		
												os.system('cls')
												cprint("-----------------------------------------\n|          (Delete Patient Record)      |\n-----------------------------------------",  "green", attrs=["bold"], file=sys.stderr)												
												patient_ID = int(input("Enter patient ID : "))
												while patient_ID not in Patients_DataBase :
													patient_ID = int(input("Incorrect ID, Please Enter valid patient ID : "))
												Patients_DataBase.pop(patient_ID)
												cprint("----------------------Patient data deleted successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
											except :
												print("Patient ID should be an Integer number")
										
								elif Admin_choice == "4" :						 				
											try :		
												os.system('cls')
												cprint("-----------------------------------------\n|          (Edit Patient Record)        |\n-----------------------------------------",  "green", attrs=["bold"], file=sys.stderr)
												patient_ID=int(input("Enter patient ID : "))
												while patient_ID not in Patients_DataBase :
													patient_ID = int(input("Incorrect ID, Please Enter valid patient ID : "))
												while True :
													cprint("------------------------------------------",  "green", attrs=["bold"], file=sys.stderr)
													cprint("|To Edit pateint Department (Enter 1) :   |",  "green", attrs=["bold"], file=sys.stderr)
													cprint("|To Edit Doctor following case (Enter 2): |",  "green", attrs=["bold"], file=sys.stderr)
													cprint("|To Edit patient Name (Enter 3) :         |",  "green", attrs=["bold"], file=sys.stderr)
													cprint("|To Edit patient Age (Enter 4) :          |",  "green", attrs=["bold"], file=sys.stderr)
													cprint("|To Edit patient Gender (Enter 5) :       |",  "green", attrs=["bold"], file=sys.stderr)
													cprint("|To Edit patient Address (Enter 6) :      |",  "green", attrs=["bold"], file=sys.stderr)
													cprint("|To Edit patient RoomNumber (Enter 7) :   |",  "green", attrs=["bold"], file=sys.stderr)
													cprint("|To be Back (Enter E)                     |",  "green", attrs=["bold"], file=sys.stderr)
													cprint("-------------------------------------------",  "green", attrs=["bold"], file=sys.stderr)
													cprint("\nEnter your choice", "magenta", attrs=["underline"], file=sys.stderr)
													Admin_choice = input(":=> ")
													Admin_choice = Admin_choice.upper()
													if Admin_choice == "1" :
														Patients_DataBase[patient_ID][0]=input("\nEnter patient department : ")
														cprint("----------------------Patient Department edited successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
														
													elif Admin_choice == "2" :
														Patients_DataBase[patient_ID][1]=input("\nEnter Doctor follouing case : ")
														cprint("----------------------Doctor follouing case edited successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
										
													elif Admin_choice == "3" :
														Patients_DataBase[patient_ID][2]=input("\nEnter patient name : ")
														cprint("----------------------Patient name edited successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
													
													elif Admin_choice == "4" :
														Patients_DataBase[patient_ID][3]=input("\nEnter patient Age : ")
														cprint("----------------------Patient age edited successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
												
													elif Admin_choice == "5" :
														Patients_DataBase[patient_ID][4]=input("\nEnter patient gender : ")
														cprint("----------------------Patient address gender successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
														
													elif Admin_choice == "6" :
														Patients_DataBase[patient_ID][5]=input("\nEnter patient address : ")
														cprint("----------------------Patient address edited successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
														
													elif Admin_choice == "7" :
														Patients_DataBase[patient_ID][6]=input("\nEnter patient RoomNumber : ")
														cprint("----------------------Patient Room Number edited successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
												
													elif Admin_choice == "E" :
														break
														
													else :
														cprint("Please Enter a correct choice", "red", attrs=["bold"], file=sys.stderr)
											except :
												cprint("Patient ID should be an Integer number", "red", attrs=["bold"], file=sys.stderr)
																				
								elif Admin_choice == "E" :										
											break
								
								else :
											cprint("Please enter a correct option\n", "red", attrs=["bold"], file=sys.stderr)					
						elif AdminOptions == "2" :	#Doctors 
							os.system('cls')
							cprint("-----------------------------------------", "yellow", attrs=["bold"], file=sys.stderr)
							cprint("|          (Doctors Menu)               |",  "yellow", attrs=["bold"], file=sys.stderr)
							cprint("-----------------------------------------",  "yellow", attrs=["bold"], file=sys.stderr)
							cprint("-------------------------------------------",  "yellow", attrs=["bold"], file=sys.stderr)
							cprint("|To add new doctor (Enter 1)              |",  "yellow", attrs=["bold"], file=sys.stderr)
							cprint("|To display doctor (Enter 2)              |",  "yellow", attrs=["bold"], file=sys.stderr)
							cprint("|To delete doctor data (Enter 3)          |",  "yellow", attrs=["bold"], file=sys.stderr)
							cprint("|To edit doctor data (Enter 4)            |",  "yellow", attrs=["bold"], file=sys.stderr)
							cprint("|To be back (Enter E)                     |",  "yellow", attrs=["bold"], file=sys.stderr)
							cprint("-------------------------------------------",  "yellow", attrs=["bold"], file=sys.stderr)
							cprint("\nEnter your choice", "magenta", attrs=["underline"], file=sys.stderr)
							Admin_choice = input (":=> ")
							Admin_choice = Admin_choice.upper()
							
							if Admin_choice == "1" : 											
									cprint("-----------------------------------------\n|          (Add Doctor's Record)         |\n-----------------------------------------", "yellow", attrs=["bold"], file=sys.stderr)
									try :
										os.system('cls')		
										Doctor_ID = int(input("Enter doctor ID : "))
										while Doctor_ID in Doctors_DataBase :			
											Doctor_ID = int(input("This ID is unavailable, please try another ID : "))
										
										Department=input("Enter Doctor department : ")
										Name      =input("Enter Doctor name       : ")
										Address   =input("Enter Doctor address    : ")
										Doctors_DataBase[Doctor_ID]=[[Department,Name,Address]]
										cprint("----------------------Doctor added successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
									except :
										print("Doctor ID should be an integer number")
								
							elif Admin_choice == "2" :
									cprint("-----------------------------------------\n|          (Search Doctor's Record)      |\n-----------------------------------------", "yellow", attrs=["bold"], file=sys.stderr)												 									
									try :
										os.system('cls')		
										Doctor_ID = int(input("Enter doctor ID : "))
										while Doctor_ID not in Doctors_DataBase :
											Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
										print("Doctor name    : ",Doctors_DataBase[Doctor_ID][0][1])
										print("Doctor address : ",Doctors_DataBase[Doctor_ID][0][2])
										print("Doctor is in "+Doctors_DataBase[Doctor_ID][0][0]+" department")
									except :
										print("Doctor ID should be an integer number")
							
							elif Admin_choice == "3" :	
									cprint("-----------------------------------------\n|          (Delete Doctor's Record)      |\n-----------------------------------------", "yellow", attrs=["bold"], file=sys.stderr)																					
									try :
										os.system('cls')		
										Doctor_ID = int(input("Enter doctor ID : "))
										while Doctor_ID not in Doctors_DataBase :
											Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
										Doctors_DataBase.pop(Doctor_ID)
										cprint("/----------------------Doctor data deleted successfully----------------------/", "magenta", attrs=["bold"], file=sys.stderr)
									except :
										print("Doctor ID should be an integer number")

							elif Admin_choice == "4" :
									os.system('cls')
									cprint("-----------------------------------------\n|          (Edit Doctor's Record)        |\n-----------------------------------------", "yellow", attrs=["bold"], file=sys.stderr)											
									try :		
										Doctor_ID=input("Enter doctor ID : ")
										while Doctor_ID not in Doctors_DataBase :
											Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
										cprint("-------------------------------------------",  "yellow", attrs=["bold"], file=sys.stderr)
										cprint("|To Edit doctor's department (Enter 1)    |",  "yellow", attrs=["bold"], file=sys.stderr)
										cprint("|To Edit doctor's name (Enter 2)          |",  "yellow", attrs=["bold"], file=sys.stderr)
										cprint("|To Edit doctor's address (Enter 3)       |",  "yellow", attrs=["bold"], file=sys.stderr)
										cprint("|To be Back (Enter E)                     |",  "yellow", attrs=["bold"], file=sys.stderr)
										cprint("-------------------------------------------",  "yellow", attrs=["bold"], file=sys.stderr)
										Admin_choice=input("Enter your choice : ")
										Admin_choice = Admin_choice.upper()
										if Admin_choice == "1" :
											Doctors_DataBase[Doctor_ID][0][0]=input("Enter Doctor's Department : ")
											cprint("/----------------------Doctor's department edited successfully----------------------/", "magenta", attrs=["bold"], file=sys.stderr)
											
										elif Admin_choice == "2" :
											Doctors_DataBase[Doctor_ID][0][1]=input("Enter Doctor's Name : ")
											cprint("----------------------Doctor's name edited successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
											
										elif Admin_choice == "3" :
											Doctors_DataBase[Doctor_ID][0][2]=input("Enter Doctor's Address : ")
											cprint("----------------------Doctor's address edited successfully----------------------", "magenta", attrs=["bold"], file=sys.stderr)
										
										elif Admin_choice == "E" :
											break
										
										else :
											cprint("\nPlease enter a correct option\n", "red", attrs=["bold"], file=sys.stderr)
											
									except :
										print("Doctor ID should be an Integer number")
											
							elif Admin_choice == "E" :											
										break
									
							else :
								cprint("\nPlease enter a correct option\n", "red", attrs=["bold"], file=sys.stderr)
											
						elif AdminOptions == "3" :
							os.system('cls')
							cprint("-----------------------------------------", "cyan", attrs=["bold"], file=sys.stderr)
							cprint("|          (Appointment Menu)           |", "cyan", attrs=["bold"], file=sys.stderr)
							cprint("-----------------------------------------", "cyan", attrs=["bold"], file=sys.stderr)															
							cprint("-------------------------------------------", "cyan", attrs=["bold"], file=sys.stderr)
							cprint("|To book an appointment (Enter 1)         |", "cyan", attrs=["bold"], file=sys.stderr)
							cprint("|To edit an appointment (Enter 2)         |", "cyan", attrs=["bold"], file=sys.stderr)
							cprint("|To cancel an appointment (Enter 3)       |", "cyan", attrs=["bold"], file=sys.stderr)
							cprint("|To be back (Enter E)                     |", "cyan", attrs=["bold"], file=sys.stderr)
							cprint("-------------------------------------------", "cyan", attrs=["bold"], file=sys.stderr)
							cprint("\nEnter your choice", "magenta", attrs=["underline"], file=sys.stderr)
							Admin_choice = input (":=> ")
							Admin_choice = Admin_choice.upper()
							if Admin_choice == "1" :																		
								try :
										os.system('cls')
										print("-----------------------------------------\n|          (Book Appointment)           |\n-----------------------------------------")													
										Doctor_ID = int(input("Enter the ID of doctor : "))
										while Doctor_ID not in Doctors_DataBase :
											Doctor_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID : "))
										print("---------------------------------------------------------")
										print("|For book an appointment for an exist patient (Enter 1) |\n|For book an appointment for a new patient (Enter 2)    |\n|To be Back (Enter E)                                   |")
										print("---------------------------------------------------------")
										Admin_choice = input ("Enter your choice : ")
										Admin_choice = Admin_choice.upper()
										if Admin_choice == "1" :
												patient_ID = int(input("Enter patient ID : "))
												while patient_ID not in Patients_DataBase :		
													patient_ID = int(input("Incorrect ID, please Enter a correct patient ID : "))	
										
											
										elif Admin_choice == "2" :
											#os.system('cls')
											patient_ID = int(input("Enter patient ID : "))
											while patient_ID in Patients_DataBase :		
												patient_ID = int(input("This ID is unavailable, please try another ID : "))					
											Department=Doctors_DataBase[Doctor_ID][0][0]
											DoctorName=Doctors_DataBase[Doctor_ID][0][1]
											Name      =input("Enter patient name    : ")
											Age       =input("Enter patient age     : ")
											Gender    =input("Enter patient gender  : ")
											Address   =input("Enter patient address : ")
											RoomNumber=""
											Patients_DataBase[patient_ID]=[Department,DoctorName,Name,Age,Gender,Address,RoomNumber]
										
										elif Admin_choice == "E" :
											break
											
										Session_Start = input("Session starts at : ")
										while Session_Start[ :2] == "11" or Session_Start[ :2] == "12" :
											Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
											
										for i in Doctors_DataBase[Doctor_ID] :
											if type(i[0])!=str :
												while Session_Start >= i[1] and Session_Start < i[2] :
													Session_Start = input("This appointment is already booked, Please Enter an other time for start of session : ")
										Session_End   = input("Session ends at : ")
										
										New_Appointment=list()
										New_Appointment.append(patient_ID)
										New_Appointment.append(Session_Start)
										New_Appointment.append(Session_End)
										Doctors_DataBase[Doctor_ID].append(New_Appointment)								
										print("/----------------------Appointment booked successfully----------------------/")
								except :
										print("Doctor ID should be an integer number")
					
							elif Admin_choice == "2" :												
									try :
										os.system('cls')	
										print("-----------------------------------------\n|          (Edit Appointment)           |\n-----------------------------------------")	
										patient_ID = int(input("Enter patient ID : "))						
										while patient_ID not in Patients_DataBase :
											patient_ID = int(input("Incorrect Id, Please Enter correct patient ID : "))
										try :   
												AppointmentIndex,PairKey = AppointmentIndexInDoctorsDataBase(patient_ID)
												Session_Start = input ("Please enter the new start time : ")
												while Session_Start[ :2] == "11" or Session_Start[ :2] == "12" :
													Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
													
												for i in Doctors_DataBase[Doctor_ID] :
													if type(i[0])!=str :
														while Session_Start >= i[1] and Session_Start < i[2] :
															Session_Start = input("This appointment is already booked, Please Enter an other time for start of session : ")
												Session_End = input ("Please enter the new end time : ")
												Doctors_DataBase[PairKey][AppointmentIndex]=[patient_ID,Session_Start,Session_End]							
												print("/----------------------Appointment edited successfully----------------------/")
										except :
												print("No Appointment for this patient")
									except :
										print("Doctor ID should be an integer number")
						
							elif Admin_choice == "3" :												
									try :
										os.system('cls')		
										print("-----------------------------------------\n|          (Cancel Appointment)           |\n-----------------------------------------")
										patient_ID = int(input("Enter patient ID : "))
										while patient_ID not in Patients_DataBase :
											patient_ID = int(input("Invorrect ID, Enter patient ID : "))
										try :
												AppointmentIndex,PairKey = AppointmentIndexInDoctorsDataBase(patient_ID)						
												Doctors_DataBase[PairKey].pop(AppointmentIndex)
												print("/----------------------Appointment canceled successfully----------------------/")
										except :
												print("No Appointment for this patient")
									except :	 
										print("Patient ID should be an integer number")
							
							elif Admin_choice == "E" :												
										break
							
							else :
										print("please enter a correct choice")
						
						elif AdminOptions == "E" :															
							break
						
						else :
							print("Please enter a correct option")
					
				
					elif Password != "1234" :
						if tries < 2 :
							Password = input("Password incorrect, please try again : ")
							tries += 1
						else :
							print("Incorrect password, no more tries\nSystem exit in 5 sec")
							tries_flag = "Close the program"
							exit_screen()
							sys.exit()
							#break
				
					Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
					Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)
					
					
		elif Admin_user_mode == "2" :	
			os.system('cls')																	#Usermode
			print("****************************************\n|         Welcome to user mode         |\n****************************************")
			while True :
				print("\n-----------------------------------------")
				print("|To view hospital's departments (Enter 1) |")
				print("|To view hospital's doctors (Enter 2)     |")
				print("|To view patients' residents (Enter 3)    |")
				print("|To view patient's details (Enter 4)      |")
				print("|To view doctor's appointments (Enter 5)  |")
				print("|To be Back (Enter E)                     |")
				print("-------------------------------------------")
				cprint("\nEnter your choice", "magenta", attrs=["underline"], file=sys.stderr)
				UserOptions = input(":=> ")
				UserOptions = UserOptions.upper()
				
				if   UserOptions == "1" :
							os.system('cls')											
							print("Hospital's departments :")
							for i in Doctors_DataBase :
								print("	"+Doctors_DataBase[i][0][0])
					
				elif UserOptions == "2" :
							os.system('cls')											
							print("Hospital's doctors :")
							for i in Doctors_DataBase :
								print("	"+Doctors_DataBase[i][0][1]+" in "+Doctors_DataBase[i][0][0]+" department, from "+Doctors_DataBase[i][0][2])
								
				elif UserOptions == "3" :
					os.system('cls')											
					for i in Patients_DataBase :
						print("	Patient : "+Patients_DataBase[i][2]+" in "+Patients_DataBase[i][0]+" department and followed by "+Patients_DataBase[i][1]+", age : "+Patients_DataBase[i][3]+", from : "+Patients_DataBase[i][5]+", RoomNumber : "+Patients_DataBase[i][6])
				
				elif UserOptions == "4" :											
					try :
						os.system('cls')				
						patient_ID = int(input("Enter patient's ID : "))
						while patient_ID not in Patients_DataBase :
							patient_ID = int(input("Incorrect Id, Please enter patient ID : "))
						print("	patient name        : ",Patients_DataBase[patient_ID][2])
						print("	patient age         : ",Patients_DataBase[patient_ID][3])
						print("	patient gender      : ",Patients_DataBase[patient_ID][4])
						print("	patient address     : ",Patients_DataBase[patient_ID][5])
						print("	patient room number : ",Patients_DataBase[patient_ID][6])
						print("	patient is in "+Patients_DataBase[patient_ID][0]+" department")
						print("	patient is followed by doctor : "+Patients_DataBase[patient_ID][1])
					except :
						print("Patient ID should be an integer number")
							
				elif UserOptions == "5" :											
					try :
						os.system('cls')				
						Doctor_ID = int(input("Enter doctor's ID : "))
						while Doctor_ID not in Doctors_DataBase :
							Doctor_ID = int(input("Incorrect Id, Please enter doctor ID : "))
						print(Doctors_DataBase[Doctor_ID][0][1]+" has appointments :")
						for i in Doctors_DataBase[Doctor_ID] :
							if type(i[0])==str :
								continue
							else :
								print("	from : "+i[1]+"    to : "+i[2])
					except :
						print("Doctor ID should be an integer number")
					
				elif UserOptions == "E" :											
					break
					
				else :
					print("Please Enter a correct choice")
					
					
		else :
			print("Please choice just 1 or 2")