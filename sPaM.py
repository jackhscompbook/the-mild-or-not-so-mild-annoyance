

#use os to do file maipulation.
import os
import time
import sys



#define spam so this can be used as a module ( I may dev it more.)
def spam():

	# infinite loop bois
	while True:
	
		# define mode and make it lower
		mode = str(input('Mode [help for help]:')).lower()


		# display help if mode is help.
		if mode == 'help':

			print('This is an annoyance util that i just made to mess with some kid who never signs out in my computer class.')
			print('''Modes are:\n1. [limted {1}]\n2. [endless {2}]\nLimeted:\nIn this mode, you enter a number of files to be created.\nEndless:
				In this mode, it just goes and goes.
				''')
			continue

		# If the mode is limeted, use the limeted mode
		elif mode == 'limeted' or mode == '1':

			start = time.time()

			# get the message and number of files.
			msg = str(input('message to be in files: '))
			num = str(input('Number of files:'))

			# create a test file for dev reasons.
			os.system('mkdir test\\')

			# loop through all numbers up to num and use each as a filename.
			for i in range(int(num)):

				# write to a file using echo
				os.system('echo ' + msg + ' > test\\' + str(i) + '.txt')

				#status msgs
				print('[*] File ' + str(i + 1) + ' created!')
			print('[*] done!')


			end = time.time()

			eTS = round((end - start), 5)
			eTM = round(((end - start)/60), 5)
			eTH = round((((end - start)/60)/60), 5)

			print('Elapsed Time: \nSec: ' + str(eTS) + '\nMin: ' + str(eTM) + \
			      '\nHrs: ' + str(eTH))


			input('...')

		elif mode == 'endless' or mode == '2':
			msg = input('message: ')
			i = 0
			while True:
				os.system('echo ' + msg + ' > test\\' + str(i) + '.txt')
				i += 1
				print('[*] File ' + str(i) + 'created!')

		elif mode == 'exit' or mode == '3':
			sys.exit()

		else:
			print('bad mode')
			continue


if __name__ == '__main__':
	spam()
