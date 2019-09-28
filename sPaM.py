

#use os to do file maipulation.
import os


#define spam so this can be used as a module ( I may dev it more.)
def spam():

	# infinite loop bois
	while True:
	
		# define mode and make it lower
		mode = input('Mode [help for help]:').lower()


		# display help if mode is help.
		if mode == 'help':

			print('This is an annoyance util that i just made to mess with some kid who never signs out in my computer class.')
			print('''Modes are:\n1. [limted]\n2. [endless]\nLimeted:\nIn this mode, you enter a number of files to be created.\nEndless:
				In this mode, it just goes and goes.
				''')
			continue

		# If the mode is limeted, use the limeted mode
		elif mode == 'limeted':

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
			input('...')

		elif mode == 'endless':
			print('coming soon....')

		else:
			print('bad mode')
			continue


if __name__ == '__main__':
	spam()
