from urllib.request import urlopen
from wget import download
from sys import argv
from re import findall


banner = '''
            \033[31m;;;;;;;;;;;;;;;;;;;;\033[37m                                                                    
          \033[31m;;;;;;;;;;;;;;;;;;;;;;;;\033[37m   ###   ##              ########       ##                        
          \033[31m;;;;;;;;;;;;;;;;;;;;;;;;\033[37m   ###   ##              ########       ##                        
          \033[31m;;;;;;;;;;;;;;;;;;;;;;;;\033[37m    ##  ###                 ##          ##                        
          \033[31m;;;;;;;;;;;;;;;;;;;;;;;;;\033[37m   ##  ###                 ##          ##                        
         \033[31m;;;;;;;;;;\033[37mG\033[31m;;;;;;;;;;;;;;;\033[37m   ### ##  ####   ##  ###  ##  ##  ### ## ###    ###             
         \033[31m;;;;;;;;;;\033[37mG##\033[31m;;;;;;;;;;;;;\033[37m    ## ## ######  ##  ###  ##  ##  ### #######  #####            
         \033[31m;;;;;;;;;;\033[37mG####\033[31m;;;;;;;;;;;\033[37m    ## ## ### ##  ##  ###  ##  ##  ### ### ### ### ###           
         \033[31m;;;;;;;;;;\033[37mG#####\033[31m;;;;;;;;;;\033[37m    ####  ##  ### ##  ###  ##  ##  ### ##  ### ### ###           
         \033[31m;;;;;;;;;;\033[37mG#####\033[31m;;;;;;;;;;\033[37m    ####  ##  ### ##  ###  ##  ##  ### ##  ### ### ###           
         \033[31m;;;;;;;;;;\033[37mG####\033[31m;;;;;;;;;;;\033[37m     ###  ##  ### ##  ###  ##  ##  ### ##  ### #######           
         \033[31m;;;;;;;;;;\033[37mG##\033[31m;;;;;;;;;;;;;\033[37m     ###  ##  ### ##  ###  ##  ##  ### ##  ### #######           
         \033[31m;;;;;;;;;;\033[37mG\033[31m;;;;;;;;;;;;;;;\033[37m     ###  ##  ### ##  ###  ##  ##  ### ##  ### ###               
          \033[31m;;;;;;;;;;;;;;;;;;;;;;;;;\033[37m     ###  ##  ### ##  ###  ##  ##  ### ##  ### ### ###           
          \033[31m;;;;;;;;;;;;;;;;;;;;;;;;\033[37m      ###  ### ##  ### ###  ##  ##  ### ### ### ### ###           
          \033[31m;;;;;;;;;;;;;;;;;;;;;;;;\033[37m      ###  ######  #### ##  ##  ####### #######  #####            
           \033[31m;;;;;;;;;;;;;;;;;;;;;;\033[37m       ###   ####    ### ##  ##   ## ### ## ###    ###             
            \033[31m;;;;;;;;;;;;;;;;;;;;\033[0m                                                                    
'''

def get_results(query):
	
	prefix = 'https://vid.puffyan.us/watch?v='
	html = urlopen('https://vid.puffyan.us/search?q='+ query)
	video_ids = findall(r'watch\?v=(\S{11})',html.read().decode())
	a = 0
	for x in video_ids:
		a = a+1
		print('['+str(a)+']'+prefix + x)
		
	print('\nshowing the top '+str(a)+' results\n')
		
	selection = input('which one do you want to watch or download ? (r:research/q:quit/v:video_number):')
		
	if selection == 'r':
		search_query = str(input('>>enter a query:'))
		get_results(search_query)
		
	elif selection == 'q':
		exit()
		
	elif selection == 'v':
		number = int(input('>>enter:'))
		print('\n')
		link = (prefix + video_ids[number])
		print(link + '\n')
		download_the_video(link)

def download_the_video(url):

	meta = urlopen('https://projectlounge.pw/ytdl/download?url='+url+'\n')

	u = meta.info()
	
	file_size = str(round((float(''.join(u.get_all("Content-Length")))/1000**2),2))+' mb'
	
	yn = input('do you want to download the video (size:'+file_size+')(y/n):')
	
	if yn == 'y':
		filename = download('https://projectlounge.pw/ytdl/download?url='+url)
		selection2 = input('\n\n'+ filename + ' downloaded succsesfully'+'(r:research/q:quit):')
		if selection2 == 'r':
			search_query = str(input('>>enter a query:'))
			get_results(search_query)
		
		elif selction2 == 'q':
			exit()
			
		else:
			exit()
		
	elif yn == 'n':
		selection3 = input('\n'+'(r:research/q:quit):')
		if selection3 == 'r':
			search_query = str(input('>>enter a query:'))
			get_results(search_query)
		
		elif selction3 == 'q':
			exit()
			
		else:
			exit()
	else:
		selection3 = input('\n'+'(r:research/q:quit):')
		if selection3 == 'r':
			search_query = str(input('>>enter a query:'))
			get_results(search_query)
		
		elif selction3 == 'q':
			exit()
			
		else:
			exit()
if len(argv) <= 1:

	print(banner)
	print('\nauthor: Ahmet Yigit AYDENIZ\n')

else:
	
	query = argv[1]
	print(banner)	
	get_results(query)
	
	
	
	str(round(float(''.join(u.get_all("Content-Length")))/1000**2),2)+' mb'
