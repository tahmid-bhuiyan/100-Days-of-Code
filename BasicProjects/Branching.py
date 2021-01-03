
#Defines the blood pressure function that acts on imput for systolic/diastolic
def blood_pressure(systolic, diastolic):
	#If systolic and diastolic meet conditions, execute, if not, move on
	if systolic < 120 and diastolic < 80: 
		risk_level = 1.0 #Sets value of lowest risk level
		#Calculates mean pressure using imputted parameters
		mean_pressure = (systolic + 2 * diastolic) / 3 
#Calculates blood pressure by multiplying risk and mean_pressure and rounding
		final = round(float(risk_level * mean_pressure), 2)
		return final #Returns final blood pressure value
	#If systolic and diastolic meet conditions, execute, if not, move on
	elif systolic >= 120 and systolic <= 129 and diastolic < 80:
		risk_level = 1.1 #Sets value of risk level
		#Calculates mean pressure using imputted parameters
		mean_pressure = (systolic + 2 * diastolic) / 3
#Calculates blood pressure by multiplying risk and mean_pressure and rounding
		final = round(float(risk_level * mean_pressure), 2)
		return final #Returns final blood pressure value
	#If systolic or diastolic meet conditions, execute, if not, move on
	elif systolic >= 140 or diastolic >= 90:
#If systolic or diastolic further meet conditions, execute, if not, move on
		if systolic >= 180 or diastolic >= 120:
			risk_level = 1.4 #Sets value of risk level
		#Calculates mean pressure using imputted parameters
			mean_pressure = (systolic + 2 * diastolic) / 3
#Calculates blood pressure by multiplying risk and mean_pressure and rounding
			final = round(float(risk_level * mean_pressure), 2)
			return final #Returns final blood pressure value
		else: #Because all other conditions weren't met, execute this
			risk_level = 1.3 #Sets value of risk level
		#Calculates mean pressure using imputted parameters
			mean_pressure = (systolic + 2 * diastolic) / 3
#Calculates blood pressure by multiplying risk and mean_pressure and rounding
			final = round(float(risk_level * mean_pressure), 2)
			return final #Returns final blood pressure value
	#If systolic or diastolic meet conditions, execute, if not, move on
	elif 130 <= systolic <= 139 or diastolic >= 80:
	#If diastolic meet conditions, execute, if not, move on
		if diastolic >= 90: 
	#If diastolic meet conditions, execute, if not, move on
			if diastolic >= 120:
				risk_level = 1.4 #Sets value of risk level
		#Calculates mean pressure using imputted parameters
				mean_pressure = (systolic + 2 * diastolic) / 3
#Calculates blood pressure by multiplying risk and mean_pressure and rounding
				final = round(float(risk_level * mean_pressure), 2)
				return final #Returns final blood pressure value
	#Because all other conditions weren't met, execute this
			else:
				risk_level = 1.3 #Sets value of risk level
		#Calculates mean pressure using imputted parameters
				mean_pressure = (systolic + 2 * diastolic) / 3
#Calculates blood pressure by multiplying risk and mean_pressure and rounding
				final = round(float(risk_level * mean_pressure), 2)
				return final #Returns final blood pressure value
	#Because all other conditions weren't met, execute this
		else:
			risk_level = 1.2 #Sets value of risk level
		#Calculates mean pressure using imputted parameters
			mean_pressure = (systolic + 2 * diastolic) / 3
#Calculates blood pressure by multiplying risk and mean_pressure and rounding
			final = round(float(risk_level * mean_pressure), 2)
			return final #Returns final blood pressure value
			
#Defines standard BMI function that acts on imput for weight,height,and ISU
def standard_BMI(weight, height, ISU):
	if ISU == True: #If ISU is true, execute, if not, move on
	#Calculates BMI using imputted parameters for weight and height
		BMI = round((weight / height**2), 2)
		return BMI #Returns calculated value for BMI
	else: #Because previous function was not met, execute
	#Converts weight from ounces to kilos
		weight = weight / 35
	#Converts height from inches to meters
		height = height * .025
	#Calculates BMI using imputted parameters for weight and height
		BMI = round((weight / height**2), 2)
		return BMI #Returns calculated value for BMI
#ISU must be true because weight must be in kilos and height in meters
ISU = True
#Defines BMI chart function that acts on imput for weight,height,age & gender
def BMI_chart(weight, height, age, gender):
#Calls on standard BMI function and its calculated BMI value
	x = standard_BMI(weight, height, ISU)
#If age meets conditions, execute, if not, move on
	if age >= 18:
		if x < 18.5: #If BMI meets conditions, execute, if not, move on
			return 'underweight' #Returns description of BMI
		#If BMI meets conditions, execute, if not, move on
		elif 18.5 <= x <= 25:
			return 'normal' #Returns description of BMI
		#If BMI meets conditions, execute, if not, move on
		elif 25 < x <= 30:
			return 'overweight' #Returns description of BMI
		#If BMI meets conditions, execute, if not, move on
		elif x > 30:
			return 'obese' #Returns description of BMI
#If age/gender meets conditions, execute, if not, move on
	elif age < 18 and gender == 'male':
	#If BMI meets conditions, execute, if not, move on
		if x < 14:
			return 'underweight' #Returns description of BMI
	#If BMI meets conditions, execute, if not, move on
		elif 14 <= x <= 19:
			return 'normal' #Returns description of BMI
	#If BMI meets conditions, execute, if not, move on
		elif 19 < x <= 22:
			return 'overweight' #Returns description of BMI
	#If BMI meets conditions, execute
		elif x > 22:
			return 'obese' #Returns description of BMI
#If age/gender meets conditions, execute, if not, move on
	elif age < 18 and gender == 'female':
	#If BMI meets conditions, execute, if not, move on
		if x < 15:
			return 'underweight' #Returns description of BMI
	#If BMI meets conditions, execute, if not, move on
		elif 15 <= x <= 20:
			return 'normal' #Returns description of BMI
	#If BMI meets conditions, execute, if not, move on
		elif 20 < x <= 23:
			return 'overweight' #Returns description of BMI
	#If BMI meets conditions, execute
		elif x > 23:
			return 'obese' #Returns description of BMI
#Defines HCT function that acts on imput for red,total cells,age,gender
def HCT(red_cells, total_cells, age, gender):
#Calculates value of volume
	vol = red_cells / total_cells
#If total_cells meets conditions, execute, if not, move on
	if total_cells < 1000000:
		return False
#If age meets conditions, execute, if not, move on
	elif age >= 18:
#If gender meets conditions, execute, if not, move on
		if gender == 'male':
#If volume meets conditions, execute, if not, move on
			if .407 <= vol <= .503:
#Since conditions for volume were met, return true
				return True
			else: #Must execute
#Since conditions for volume weren't met, return false
				return False
#If gender meets conditions, execute
		elif gender == 'female':
			if .361 <= vol <= .443:
#Since conditions for volume were met, return true
				return True
			else: #Must execute
#Since conditions for volume weren't met, return false
				return False
#If age meets conditions, execute, if not, move on
	elif age < 18:
#If volume meets conditions, execute, if not, move on
		if .36 <= vol <= .4:
#Since conditions for volume were met, return true
			return True
		else: #Must execute
#Since conditions for volume weren't met, return false
			return False

#Defines HCT function that acts on imput for red,total cells,age,gender
def LDL(total, HDL, trig, age, gender):
#If age total and trig meet conditions, execute, if not, move on
	if total > 250 and trig > 43.5:
#Calculates value of k
		k = .19 - ((total - 250) // 10 * .01)
#Calculates value of LDL
		LDL = total - HDL - trig * k
#If age meets conditions, execute, if not, move on
		if age >= 18:
#If gender and HDL meets conditions, execute, if not, move on
			if gender == 'male' and HDL < 40:
#If LDL meets conditions, execute, if not, move on
				if LDL < 120:
#Sets value of risk to 0
					risk = 0
					return risk + 1 #Returns value of risk plus one
#If age meets conditions, execute, if not, move on
				elif LDL >= 120:
					risk = 1 + (LDL - 120) // 20
					return risk + 1 #Returns value of risk plus one
#If gender and HDL meets conditions, execute, if not, move on
			elif gender == 'female' and HDL < 50:
#If LDL meets conditions, execute, if not, move on
				if LDL < 120:
#Sets value of risk to 0
					risk = 0
					return risk + 1 #Returns value of risk plus one
#If LDL meets conditions, execute, if not, move on
				elif LDL >= 120:
					risk = 1 + (LDL - 120) // 20
					return risk + 1 #Returns value of risk plus one
			elif HDL > 70:
#If LDL meets conditions, execute, if not, move on
				if LDL < 120:
#Sets value of risk to 0
					risk = 0
					return risk - 1 #Returns value of risk minus one
#If LDL meets conditions, execute, if not, move on
				elif LDL >= 120:
					risk = 1 + (LDL - 120) // 20
					return risk - 1 #Returns value of risk minus one
#If LDL meets conditions, execute, if not, move on
			elif LDL < 120:
#Sets value of risk to 0
				risk = 0
				return risk #Returns value of risk
#If LDL meets conditions, execute, if not, move on
			elif LDL >= 120:
				risk = 1 + (LDL - 120) // 20
				return risk #Returns value of risk
		if age < 18:
#If LDL meets conditions, execute, if not, move on
			if LDL < 100:
#Sets value of risk to 0
				risk = 0
				return risk #Returns value of risk
#If LDL meets conditions, execute, if not, move on
			elif LDL >= 100:
				risk = 1 + (LDL - 100) // 15
				return risk #Returns value of risk
	elif trig < 11.3 or trig > 43.5:
		k = 0 #Sets value of k
		LDL = total - HDL - trig * k	
#If age meets conditions, execute, if not, move on
		if age >= 18:
			if gender == 'male' and HDL < 40:
#If LDL meets conditions, execute, if not, move on
				if LDL < 120:
#Sets value of risk to 0
					risk = 0 #Sets value of risk
					return risk + 1 #Returns value of risk plus one
#If LDL meets conditions, execute, if not, move on
				elif LDL >= 120:
#Calculates value of risk
					risk = 1 + (LDL - 120) // 20
					return risk + 1 #Returns value of risk plus one
			elif gender == 'female' and HDL < 50:
#If LDL meets conditions, execute, if not, move on
				if LDL < 120:
					risk = 0 #Sets value of risk
					return risk + 1 #Returns value of risk plus one
#If LDL meets conditions, execute, if not, move on
				elif LDL >= 120:
#Calculates value of risk
					risk = 1 + (LDL - 120) // 20
					return risk + 1 #Returns value of risk plus one
			elif HDL > 70:
#If LDL meets conditions, execute, if not, move on
				if LDL < 120:
					risk = 0 #Sets value of risk
					return risk - 1 #Returns value of risk minus one
#If LDL meets conditions, execute, if not, move on
				elif LDL >= 120:
#Calculates value of risk
					risk = 1 + (LDL - 120) // 20
					return risk - 1 #Returns value of risk minus one
#If LDL meets conditions, execute, if not, move on
			elif LDL < 120:
				risk = 0 #Sets value of risk
				return risk #Returns value of risk
#If LDL meets conditions, execute, if not, move on
			elif LDL >= 120:
#Calculates value of risk
				risk = 1 + (LDL - 120) // 20
				return risk #Returns value of risk
#If age meets conditions, execute, if not, move on
		if age < 18:
#If LDL meets conditions, execute, if not, move on
			if LDL < 100:
				risk = 0 #Sets value of risk
				return risk #Returns value of risk
#If LDL meets conditions, execute, if not, move on
			elif LDL >= 100:
#Calculates value of risk
				risk = 1 + (LDL - 100) // 15
				return risk #Returns value of risk
#If trig meets conditions, execute
	elif 11.3 <= trig <= 43.5:
#Calculates the value of LDL
		LDL = total - HDL - trig * .2
#If age meets conditions, execute, if not, move on
		if age >= 18:
#If gender/HDL meets conditions, execute, if not, move on
			if gender == 'male' and HDL < 40:
#If LDL meets conditions, execute, if not, move on
				if LDL < 120:
					risk = 0 #Sets value of risk
					return risk + 1 #Returns value of risk plus one
#If LDL meets conditions, execute, if not, move on
				elif LDL >= 120:
#Calculates value of risk
					risk = 1 + (LDL - 120) // 20
					return risk + 1 #Returns value of risk plus one
			elif gender == 'female' and HDL < 50:
#If LDL meets conditions, execute, if not, move on
				if LDL < 120:
					risk = 0 #Sets value of risk
					return risk + 1 #Returns value of risk plus one
#If LDL meets conditions, execute, if not, move on
				elif LDL >= 120:
					risk = 1 + (LDL - 120) // 20
					return risk + 1 #Returns value of risk plus one
			elif HDL > 70:
#If LDL meets conditions, execute, if not, move on
				if LDL < 120:
					risk = 0 #Sets value of risk
					return risk - 1 #Returns value of risk minus one
#If LDL meets conditions, execute, if not, move on
				elif LDL >= 120:
#Calculates value of risk
					risk = 1 + (LDL - 120) // 20
					return risk - 1 #Returns value of risk minus one
#If LDL meets conditions, execute, if not, move on
			elif LDL < 120:
				risk = 0 #Sets value of risk
				return risk #Returns value of risk
#If LDL meets conditions, execute
			elif LDL >= 120:
				risk = 1 + (LDL - 120) // 20
				return risk #Returns value of risk
#If age meets conditions, execute, if not, move on
		if age < 18:
#If LDL meets conditions, execute, if not, move on
			if LDL < 100:
				risk = 0 #Sets value of risk
				return risk #Returns value of risk
#If LDL meets conditions, execute, if not, move on
			elif LDL >= 100:
#Calculates value of risk
				risk = 1 + (LDL - 100) // 15
				return risk #Returns value of risk