from numpy import ceil
from numpy import floor

def wrap(char: str, length: int, upper: bool):
	mid = length / 2
	def func(title: str):
		if upper:
			title = title.upper()
		left = ceil(len(title) / 2)
		right = floor(len(title) / 2)
		res = '//' + char * int(mid - left) + title + char * int(mid - right)
		print(res)
		
	return func
section = wrap("=", 80, True)
subsection = wrap('=', 60, False)
subsection2 = wrap('=', 40, False)
subsection3 = wrap('=', 20, False)
l_section = wrap('-', 40, False)
l_subsection = wrap('-', 20, False)

end = section('')
subend = subsection('')
subend2 = subsection2('')
subend3 = subsection3('')
l_end = l_section('')
l_subend = l_subsection('')
