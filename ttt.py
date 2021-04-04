import kivy
kivy.require('1.0.6')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivymd.uix.button import MDIconButton
kv=""" 
Screen:
	
	FloatLayout:
		opacity:.0
		id:game
		
		MDIconButton:
			id:exit_butt
			icon:"location-exit"
			pos_hint:{"center_x":0.9,"center_y":0.95}
			on_press:
				print("back")
				self.opacity=0
				game.opacity=0
				app_heading.opacity = 1
				home.add_widget(start_button)
				
		MDGridLayout:
			id:final
			halign:"center"
			cols:3
			rows:3
			padding:35
			spacing:40
			size_hint_y:None
			size:1000,1000
			
			adaptive_hieght : True
			pos_hint:{"center_x":0.5,"center_y":0.4}
			Mark:
				id:a
				m:1
				opacity : .4
			Mark:
				opacity : .4
				m:2
				id:b
			Mark:
				m:3
				opacity : .4
				id:c
			Mark:
				m:4
				opacity : .4
				id:d
			Mark:
				m:5
				opacity : .4
				id:e
			Mark:
				m:6
				opacity : .4
				id:f
			Mark:
				m:7
				opacity : .4
				id:g
			Mark:
				m:8
				opacity : .4
				id:h
			Mark:
				m:9
				opacity : .4
				id:i
		MDFillRoundFlatButton:
			id:reset_butt
			markup: True
			text:"[size=70]reset[/size]"
			custom_color: .1, .0, .8 ,1
			pos_hint:{"center_x":0.8,"center_y":0.1}
			on_press:
				a.icon="alert-box-outline"
	  	  	b.icon="alert-box-outline"
	  	  	c.icon="alert-box-outline"
	  	  	d.icon="alert-box-outline"
	  	  	e.icon="alert-box-outline"
	  	  	f.icon="alert-box-outline"
	  	  	g.icon="alert-box-outline"
	  	  	h.icon="alert-box-outline"
	  	  	i.icon="alert-box-outline"
	  	  	a.opacity = .4
				b.opacity = .4
				c.opacity = .4
				d.opacity = .4
				e.opacity = .4
				f.opacity = .4
				g.opacity = .4
				h.opacity = .4
				i.opacity = .4
	  	  	
	
	MDFloatLayout:
		id:home
		MDLabel:
			id:app_heading
			markup: True
			halign:"center"
			text:'[size=150][color=ff0000] tic[/color] [color=ffff00]tac[/color] [color=00ffff]toe[/color][/size]'
			pos_hint:{"center_x":0.5,"center_y":0.7}
			
		MDTextButton:
			id:start_button
			text: "Start GAME"
	  	  custom_color: 0, .5, .5, 1
	  	  pos_hint:{"center_x":0.5,"center_y":0.3}
	  	  font_size:100
			on_press:
				print("start")
				app_heading.opacity = 0
				game.opacity = 1
				exit_butt.opacity = 1
				home.remove_widget(start_button)
				app.o_point = []
				app.x_point = []
<Mark>:
	user_font_size: "32sp"
	icon: "alert-box-outline"
	on_press:
		
		print(*app.x_point)
		if app.turn=="o" and self.icon =="alert-box-outline":self.icon = "checkbox-blank-circle-outline";app.turn = "x";app.o_point.append(self.m)
		elif app.turn =="x" and self.icon =="alert-box-outline":self.icon = "sword-cross" ;app.turn = "o";app.x_point.append(self.m); self.check_winner(app.x_point)
		self.m = 0
		self.opacity=1
		
				

"""
class Mark (MDIconButton):
	def check_winner(self,lst):
		for a in App.win_cond:
			if a[0] in lst and a[1] in lst and a[2] in lst:
				print("y")
	

class GameUI (FloatLayout):
	pass

class App(MDApp):
	x_point = []
	o_point = []
	win_cond = [(1,2,3),(4,5,6),(6,7,8),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
	turn = StringProperty("x")
	new_component = GameUI()
	
	def build (self):
		return Builder.load_string(kv)
		
App().run()