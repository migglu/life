from life import Life
from console import Console

def main():
	console = Console()
	life = Life(console.get_rows()-1, console.get_cols()/2)
	life.randomize()
	try:
		life.play()
	except KeyboardInterrupt:
		pass

if __name__ == '__main__':
	main()