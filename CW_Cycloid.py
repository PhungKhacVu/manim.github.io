from manim import *


class Cycloid(Scene):

    def construct(self):
        
        Txt = Text("Đường Cycloid với Manim", font="Palatino", color=ORANGE).scale(1).to_edge(UP)
    
        Txt1 = Text("Khắc Vũ", font="Palatino").scale(0.4).to_corner(DR)
        
        #image = ImageMobject ("ctu.png").scale(0.04).to_corner(UL)


        r = 3 / PI
        corr = 1 / config.frame_rate  # missed frame correction


        BL = NumberLine(include_numbers=True).shift(DOWN * r * 2)  # đường cơ sở
        

        C = Circle(color =YELLOW).next_to(BL.n2p(-6), UP, buff=0) # đường tròn
        DL = DashedLine(C.get_center(), C.get_top(), color=GREEN) # đường nối tâm
        CP = Dot(DL.get_start(), color=YELLOW)  # tâm đường tròn
        TP = Dot(DL.get_end(), color=PINK).scale(1.2)  # Điểm trên đường tròn

        RC = VGroup(C, DL, CP, TP)  # lăn đường tròn

        self.dir = 1  # hướng chuyển động


        def Rolling(m, dt):  # update_function
            theta = self.dir * -PI
            m.rotate(dt * theta, about_point=m[0].get_center()).shift(dt * LEFT * theta * r)

        Cycloid = TracedPath(TP.get_center, stroke_width=6.5, stroke_color=PINK)

        self.play(Write(Txt))
        self.play(Write(Txt1))
        self.play(Write(BL))
        self.play(Write(C))
        self.play(Write(CP))
        self.play(Write(TP))
        self.play(Write(DL))
        self.wait()
        self.add(BL, Txt, Txt1, Cycloid, RC)
        
        

        RC.add_updater(Rolling)
        self.wait(4 + corr)

        RC.suspend_updating(Rolling)
        Cycloid.clear_updaters()

        self.wait()
        self.dir = -1  # direction change, rolling back

        RC.resume_updating(Rolling)
        self.play(Uncreate(Cycloid, rate_func=lambda t: linear(1 - t), run_time=4 + corr))
            
        RC.clear_updaters()
        self.wait()

        

    
