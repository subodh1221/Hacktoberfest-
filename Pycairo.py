# importing pycairo 
import cairo 


# creating a SVG surface 
# here geek1 is file name & 700, 700 is dimension 
with cairo.SVGSurface("geek1.svg", 700, 700) as surface: 
	
	# creating a cairo context object 
	context = cairo.Context(surface) 
	
	#creating a rectangle(square) 
	context.rectangle(50, 50, 100, 100) 
	
	#creating a rectangle 
	context.rectangle(200, 200, 100, 50) 
	
	#stroke the context to remove the moved pen 
	context.stroke() 
	
	#creating a Arc 
	context.arc(330, 60, 40, 500, 2*22/7) 
	
	#stroke the context to remove the moved pen 
	context.stroke() 
	
	#creating a Circle 
	context.arc(500, 60, 40, 0, 2*22/7) 
	
	
	# setting scale of the context 
	context.scale(700, 700) 
	
	# setting line width of the context 
	context.set_line_width(0.0025) 
	
	# setting color of the context 
	context.set_source_rgba(0, 0, 0, 1) 
	
	# stroke out the color and width property 
	context.stroke() 
	
