"""
This code is for the normal distribution animation. Enjoy it!
The link of the video: https://www.bilibili.com/video/BV1nW4y1q7rN/
@author: Yunpengtai
@contact: yunpengtai.typ@gmail.com
"""
from manimlib import *

class Background(Scene):
    """Background Scene for the video.
       1. Introduce the background 
       2. Find the problem
    """
    def construct(self):
        title = TexText("Examination").to_corner(UL)
        exam = ImageMobject("./resources/exam.png").scale(1.40)
        self.play(
            ShowCreation(title),
            FadeIn(exam),
            run_time=2
        )
        self.wait(3)
        table = r"""
        \begin{table}[]
        \begin{tabular}{cc}\hline
        \textbf{Grade} & \textbf{Proportion} 
        \\ \hline
        A              & ?                   \\
        B              & ?                   \\
        C              & ?                   \\
        D              & ?                   
        \\ \hline
        \end{tabular}
        \end{table}
        """
        table = TexText(table).shift(3.4 * LEFT + 0.2 * UP)
        self.play(
            FadeOut(exam),
        )
        self.wait()

        self.play(
            Write(table),
        )

        rect = Rectangle(1, 2.2).shift(2.35 * LEFT + 0.1 * DOWN).set_color(RED)

        self.play(
            ShowCreation(rect)
        )
        self.wait(3)

        axes = Axes(
            x_range=(-5, 5, 1),
            y_range=(0, 1.5, 1),
            width=8,
            height=4,
            axis_config={
                "include_tip": True,
            },
        ).set_color(WHITE)

        cal_formula = lambda x: 2 / math.sqrt(math.pi) * math.e ** (-x ** 2 / 4)
        dis = axes.get_graph(cal_formula, color=BLUE).shift(3.5 * RIGHT + 0.7 * UP)
        dis_text1 = TexText("Normal Distribution").next_to(dis, 2.5 * UP).set_color(GREEN)
        dis_text2 = TexText("Bell Curve").next_to(dis, 2.5 * UP).set_color(GREEN)
        dis.set_fill(BLUE, opacity=1.)

        arrow1 = Arrow(
            rect.get_right(),
            np.array([1.57068163, 0., 0.])
        ).set_color(YELLOW)

        self.play(
            ShowCreation(dis),
        )

        self.wait(3)

        self.play(
            ShowCreation(arrow1),
        )

        self.wait(3)
        self.play(
            Write(dis_text1),
        )
        self.wait(3)

        self.play(
            TransformMatchingTex(dis_text1, dis_text2)
        )

        self.play(
            FadeOut(table),
            FadeOut(arrow1),
            FadeOut(rect),
            FadeOut(dis_text2),
            FadeOut(dis)
        )

        self.wait(3)

        axes.shift(0.72 * UP + 3.5 * RIGHT)
        labels = axes.get_axis_labels(x_label_tex='x', y_label_tex='y')
        labels[0].shift(RIGHT)
        dis.set_fill(BLUE, opacity=0.)
        dis_group = VGroup(dis, axes, labels).to_corner(UL).shift(DOWN + 0.4 * LEFT)

        dis_text1.to_corner(UL).set_color(WHITE)
        self.play(
            ShowCreation(dis_group),
            FadeTransform(title, dis_text1),
            run_time=3
        )
        self.wait(3)
        
        f_x = Tex(r"f(x) = \frac{1}{\sqrt{2\pi} \sigma} e ^ {- (\displaystyle \frac{x - \mu}{\sqrt{2}\sigma}) ^ 2}")

        f_x.to_corner(UR).shift(DOWN)

        self.play(
            Write(f_x),
        )
        self.wait(3)

        mu = Tex("\\mu").set_color(BLUE).move_to(dis_group.get_bottom())

        bottom = dis_group.get_bottom()

        self.play(
            ShowCreation(mu),
        )
        pos_tips, neg_tips = [], []

        for i in range(1, 4):
            pos = bottom + np.array([i * 0.8, 0, 0])
            neg = bottom + np.array([-i * 0.8, 0, 0])
            pos_tips.append(pos)
            neg_tips.append(neg)

        pos_sigmas = [Tex(f"{i}\\sigma").set_color(GREEN).move_to(bottom).move_to(p) for (i, p) in zip(range(2, 4), pos_tips[1:])]
        pos_sigmas.insert(0, Tex("\\sigma").set_color(GREEN).move_to(bottom).move_to(pos_tips[0]))
        neg_sigmas = [Tex(f"{-i}\\sigma").set_color(GREEN).move_to(bottom).move_to(n) for (i, n) in zip(range(2, 4), neg_tips[1:])]
        neg_sigmas.insert(0, Tex("-\\sigma").set_color(GREEN).move_to(bottom).move_to(neg_tips[0]))

        pos_sigmas = VGroup(*pos_sigmas)
        neg_sigmas = VGroup(*neg_sigmas)

        self.play(
            ShowCreation(pos_sigmas),
            ShowCreation(neg_sigmas),
        )

        F_x = Tex(r"F(x) = \int_{-\infty} ^ {+\infty} f(x) \mathrm{dx} = ?", isolate=[r'\int_{-\infty} ^ {+\infty}', '?'])
        F_x.set_color_by_tex(r'\int_{-\infty} ^ {+\infty}', GREEN).next_to(f_x, 2 * DOWN)

        self.play(
            Write(F_x)
        )
        self.wait(3)

        dxs = [1, 0.2, 0.02]
        rects = [axes.get_riemann_rectangles(dis, x_range=[-5, 5, dx]) for dx in dxs]

        self.play(
            ShowCreation(rects[0])
        )

        self.wait(3)

        self.play(
            ReplacementTransform(rects[0], rects[1]),
        )
        self.wait(3)

        self.play(
            ReplacementTransform(rects[1], rects[2]),
        )

        self.wait(3)

        F_x_2 = Tex("= 1").next_to(F_x, 2 * DOWN).shift(LEFT)
        self.play(
            FadeIn(F_x_2)
        )
        self.wait(3)

        self.clear()

        wait_how = TexText("Wait! How?").to_corner(UL)
        F_x_3 = Tex(r"F(x) = \int_{-\infty} ^ {+\infty} f(x) \mathrm{dx} = \int_{-\infty} ^ {+\infty} \frac{1}{\sqrt{2\pi} \sigma} e ^ {- (\displaystyle \frac{x - \mu}{\sqrt{2}\sigma}) ^ 2} \mathrm{dx} = 1")
        F_x_3.shift(2 * UP)

        self.play(
            Write(wait_how),
            Write(F_x_3),
            run_time=3
        )

        self.wait(3)

        F_x_4 = Tex(r"G(x) = \int_{-\infty} ^ {+\infty} g(x) \mathrm{dx} = \int_{-\infty} ^ {+\infty} \frac{1}{\sqrt{2\pi} \sigma} e ^ {- \displaystyle (\frac{x}{\sqrt{2}\sigma}) ^ 2} \mathrm{dx} = 1")
        F_x_4.next_to(F_x_3, 6 * DOWN)

        hint = Tex("\\mu = 0").set_color(BLUE).next_to(F_x_3, 2 * DOWN).shift(5 * RIGHT)

        arrow2 = Arrow(
            hint.get_bottom(),
           np.array([ 4, -0.53790242,  0.]),
        ).set_color(YELLOW)

        self.play(
            Write(F_x_4),
        )
        self.wait(3)

        rect2 = SurroundingRectangle(F_x_4, color=RED)

        self.play(
            ShowCreation(rect2),
            Write(hint),
            ShowCreation(arrow2),
        )
        self.wait(3)
        self.clear()

        final_title = TexText("More simplified").to_corner(UL)
        final_equ = Tex(r"Q = \int_{-\infty}^{+\infty} e^{-x^2} \mathrm{dx} = ?")

        self.play(
            FadeIn(final_title),
            Write(final_equ)
        )
        self.wait()

class ThreeDGraph(Scene):
    """ThreeDGraph Scene for the video.
       1. Introduce the volume 
       2. Two volume computation methods
    """
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        )        
        labels = axes.get_axis_labels(x_label_tex='x', y_label_tex='y')
        title = Tex(r"\text{The volume?}")
        title.to_corner(UL).fix_in_frame()

        title2 = Tex(r"\text{Another method?}")
        title2.to_corner(UL).fix_in_frame()

        instruct_text = Tex("\\text{Let's find }dV", isolate=['dV']).next_to(title, DOWN+RIGHT).fix_in_frame()
        disk_text = Tex("\\text{Disk Method}").to_corner(UL).shift(0.7 * DOWN).fix_in_frame()

        imply_y = Tex("\\implies \\ dy \\rightarrow 0").next_to(instruct_text, 1 * RIGHT).set_color(BLUE).fix_in_frame()
        dv = Tex("dV").next_to(instruct_text, 4 * DOWN).shift(0.5 * DOWN + 0.5 * RIGHT).fix_in_frame()
        arrow_dv = Arrow(
            [0, -1.4, 0.9],
            [0, -0.5, 0.5]
        )

        dv_shell = Tex("dV").next_to(title, 5 * DOWN + 7 * RIGHT).set_color(YELLOW).fix_in_frame()

        arrow_dv_shell = Arrow(
            [0.5, -1.4, 0.9],
            [0.05, -0.5, 0.45]
        ).set_color(YELLOW)

        dv_group = VGroup(dv, arrow_dv).set_color(YELLOW)
        disk_equ = Tex("dV = s h = A(y) dy", isolate=["A(y)"])

        disk_equ.next_to(imply_y, 2 * RIGHT).fix_in_frame()
        disk_equ.set_color_by_tex("A(y)", PURPLE)

        disk_equ2 = Tex("A(y) = \\int_{-\\infty}^{\\infty} e^{-r^2} \\mathrm{dx}", isolate=["A(y)", "e^{-r^2}"])
        disk_equ2.next_to(disk_equ, DOWN).set_color_by_tex("A(y)", PURPLE).fix_in_frame()
        disk_equ2.set_color_by_tex("e^{-r^2}", GREEN)

        disk_equ_Ay = Tex("e^{-y^2} Q dy", isolate=["e^{-y^2}", "Q", "dy"])
        disk_equ_Ay.move_to(disk_equ).shift(1.4 * RIGHT + 0.08 * UP).fix_in_frame()
        disk_equ_Ay.set_color_by_tex("e^{-y^2}", GREEN)
        disk_equ_Ay.set_color_by_tex("Q", RED)

        disk_equ3 = Tex("= \\int_{-\\infty}^{\\infty} e^{-x^2-y^2} \\mathrm{dx}", isolate=["e^{-x^2-y^2}"])
        disk_equ3.set_color_by_tex("e^{-x^2-y^2}", GREEN)
        disk_equ3.next_to(disk_equ2, DOWN).fix_in_frame()

        disk_equ4 = Tex("= e^{-y^2} \\int_{-\\infty}^{\\infty} e^{-x^2} \\mathrm{dx}", isolate=["e^{-x^2}", "e^{-y^2}"])

        disk_equ4.set_color_by_tex("e^{-x^2}", GREEN)
        disk_equ4.set_color_by_tex("e^{-y^2}", GREEN)
        disk_equ4.next_to(disk_equ3, DOWN).fix_in_frame()

        disk_equ5 = Tex("= e^{-y^2} Q", isolate=["Q", "e^{-y^2}"]).next_to(disk_equ4, DOWN).shift(LEFT).fix_in_frame()
        disk_equ5_rect = Rectangle(2.6136, 1.20).move_to(disk_equ4).shift(0.8 * RIGHT).set_color(RED).fix_in_frame()
        disk_equ5.set_color_by_tex("Q", RED).set_color_by_tex("e^{-y^2}", GREEN)

        disk_v1 = Tex("V = \\int_{-\\infty}^{\\infty} e^{-y^2} Q dy", isolate=["e^{-y^2}", "Q"])
        disk_v1.next_to(disk_equ, DOWN).set_color_by_tex("Q", RED).fix_in_frame()

        disk_v2 = Tex(" = Q \\int_{-\\infty}^{\\infty} e^{-y^2} dy", isolate=["e^{-y^2}", "Q"])
        disk_v2.next_to(disk_v1, DOWN).set_color_by_tex("Q", RED).fix_in_frame()
        disk_v2_rect = Rectangle(2.6136, 1.20).move_to(disk_v2).shift(0.5 * RIGHT).set_color(BLUE).fix_in_frame()

        disk_v3 = Tex(" = Q^2", isolate=["Q^2"])
        disk_v3.next_to(disk_v2, DOWN).set_color_by_tex("Q^2", RED).shift(1.2 * LEFT).fix_in_frame()

        rotate_text = Tex("\\text{Rotate the graph by z-axis}").to_corner(UL).shift(0.7 * DOWN).fix_in_frame()
        graph_tex = Tex("z = e ^{-x^2}").next_to(dv, 13 * RIGHT).shift(1. * UP + DOWN).set_color(GREEN).fix_in_frame()
        surface_tex = Tex("z = e ^{-r^2}").next_to(dv, 13 * RIGHT).shift(1. * UP + DOWN).set_color(GREEN).fix_in_frame()
        r_formula = Tex("r = \\sqrt{x ^ 2 + y ^ 2}").next_to(surface_tex, 2 * UP).fix_in_frame()

        arrow_dy = Arrow(
            [0.8, 1.3, 0],
            [0, 0.1, 0]
        )
        
        dy_line = Line(
            [0, 0, 0],
            [0, 0.2, 0]
        )

        dy = Tex("dy").next_to(instruct_text, 17 * DOWN + 7 * RIGHT).fix_in_frame()
        dy_group = VGroup(dy, arrow_dy, dy_line).set_color(RED)

        self.add(axes, labels)
        graph = axes.get_parametric_curve(
            lambda t: np.array([t, 0, math.e ** (-t ** 2)]),
            t_range = [-4, 4],
            color=BLUE
        )

        self.wait(3)

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=120 * DEGREES,
            phi=70 * DEGREES,
        )

        self.play(
            ShowCreation(graph), 
            FadeIn(graph_tex),
            # 在过渡期间移动相机帧
            frame.increment_phi, 5 * DEGREES,
            frame.increment_theta, 10 * DEGREES,
            run_time=3
        )
        self.wait(3)

        graph_total = ParametricSurface(
            lambda u,v: np.array([u, v, math.e ** (-(u ** 2 + v ** 2))]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            color=GREEN
        )

        self.play(
            FadeIn(rotate_text),
            Rotate(graph, 180 * DEGREES),
            ShowCreation(graph_total),
            TransformMatchingTex(graph_tex, surface_tex),
            run_time=3
        )

        self.wait(3)
        self.play(
            Write(r_formula)
        )
        self.wait()

        self.play(
            FadeIn(title),
            FadeOut(r_formula)
        )

        self.wait(3)

        # Zoom in
        self.play(
            frame.set_width, graph_total.get_width()*2.0,
            # Move the camera to the object
            frame.move_to, graph_total
        )
        self.wait(3)

        self.save_state()
        graph_extend = axes.get_parametric_curve(
            lambda t: np.array([t, 0.2, math.e ** (-t ** 2 - 0.04)]),
            t_range = [-4, 4],
            color=BLUE
        )

        volume_disk = ParametricSurface(
            lambda u,v: np.array([u, v, math.e ** (-(u ** 2 + v ** 2))]),
            u_range=[-4, 4],
            v_range=[0, 0.2],
            color=GREEN
        )

        graph_y = axes.get_parametric_curve(
            lambda t: np.array([t, 0.2, 0]),
            t_range = [-4, 4],
            color=WHITE
        )

        extend_group = VGroup(graph_extend, graph_y)
        instruct_text_copy = instruct_text.copy().to_corner(UL).shift(0.7 * DOWN)

        self.play(
            FadeTransform(rotate_text, instruct_text_copy),
        )

        self.wait(3)

        imply_copy = imply_y.copy().to_corner(UL).shift(0.7 * DOWN + 3 * RIGHT)

        self.play(
            FadeOut(graph_total),
            FadeIn(extend_group),
            FadeIn(dy_group)
        )

        self.wait(3)

        self.play(
            FadeTransform(instruct_text_copy, disk_text),
            FadeIn(imply_copy)
        )

        self.wait(3)

        self.play(
            FadeIn(volume_disk),
            graph.animate.set_fill(GREEN, opacity=1.),
            graph_extend.animate.set_fill(GREEN, opacity=1.),
        )

        self.wait(3)

        self.play(
            FadeIn(dv_group)
        )

        self.wait(3)

        self.play(
            dv.animate.shift(2.8 * LEFT + 0.3 * UP),
            dy.animate.shift(3 * LEFT),
            surface_tex.animate.shift(3 * LEFT),
            self.camera.frame.move_to, np.array((-2., 0., 0.)),
        )

        self.wait(3)

        self.play(
            Write(disk_equ),
            graph_extend.animate.set_fill(PURPLE, opacity=1.),
        )
        self.wait(3)

        self.play(
            ReplacementTransform(disk_equ.get_part_by_tex("A(y)").copy(), 
                                 disk_equ2.get_part_by_tex("A(y)")),
            FadeIn(disk_equ2)
        )
        self.wait(3)

        self.play(
            TransformMatchingTex(disk_equ2.copy(), disk_equ3),
        )

        self.wait(3)

        self.play(
            TransformMatchingTex(disk_equ3.copy(), disk_equ4),
        )

        self.wait(3)

        self.play(
            FadeIn(disk_equ5_rect)
        )

        self.wait(3)

        self.play(
            TransformMatchingTex(disk_equ4.copy(), disk_equ5),
        )

        self.wait(3)

        Ay_group = VGroup(disk_equ2, disk_equ3, disk_equ4, disk_equ5, disk_equ5_rect)
        self.play(
            FadeOut(Ay_group),
            FadeOut(disk_equ.get_part_by_tex("dy")),
            FadeTransform(disk_equ.get_part_by_tex("A(y)"), disk_equ_Ay),
        )

        self.wait(3)

        self.play(
            ShowCreation(disk_v1),
        )

        self.wait(3)

        self.play(
            TransformMatchingTex(disk_v1.copy(), disk_v2),
        )

        self.wait(3)

        self.play(
            FadeIn(disk_v2_rect)
        )

        self.wait(3)

        self.play(
            TransformMatchingTex(disk_v2.copy(), disk_v3),
        )
        self.wait(3)

        self.clear()
        self.restore()

        self.play(
            FadeOut(rotate_text),
            FadeOut(surface_tex),
            FadeTransform(title, title2),
            graph_total.animate.set_color(BLUE, opacity=0.3)
        )
        self.wait(3)

        self.play(
            frame.set_width, graph_total.get_width()*1.5,
            # Move the camera to the object
            frame.move_to, graph,
            frame.increment_phi, 10 * DEGREES,
            frame.increment_theta, 25 * DEGREES,
            run_time=3
        )
        self.wait(3)

        instruct_text2 = Tex("\\text{Cylinder Method}").to_corner(UL).shift(0.7 * DOWN).fix_in_frame()
        dis_text = Tex("\\text{Distance towards z}").next_to(instruct_text2, DOWN + 4 * RIGHT).fix_in_frame()
        r = Tex("r").next_to(dv_shell, 7 * RIGHT).set_color(YELLOW).fix_in_frame()
        dr = Tex("dr").next_to(r, 2 * RIGHT).set_color(YELLOW).fix_in_frame()

        cylinder = Cylinder(radius=0.2, height=0.9, v_range=(math.e**(-8), 1)).set_color(GREEN)
        cylinder.move_to(np.array((0., 0., 0.48)))

        cylinder1 = Cylinder(radius=0.4, height=0.9, v_range=(math.e**(-8), 1)).set_color(RED, opacity=0.8)
        cylinder1.move_to(np.array((0., 0., 0.48)))

        self.play(
            FadeOut(graph_total),
        )
        self.wait(3)

        self.play(
            FadeIn(instruct_text2),
            ShowCreation(cylinder),
            ShowCreation(cylinder1),
        )

        self.wait(3)

        self.play(
            FadeIn(graph_total)
        )

        self.wait(3)

        self.play(
            frame.increment_phi, -30 * DEGREES,
            frame.increment_theta, 10 * DEGREES
        )
        self.wait(3)

        r_line = Line(
            [-0.2, 0, math.e ** (- 0.3 ** 2)],
            [0, 0, 0.915]
        ).set_color(YELLOW)
    
        arrow_r = Arrow(
            [-0.15, 0, math.e ** (- 0.3 ** 2) + 0.5],
            [0, 0., 0.7]
        ).set_color(YELLOW)

        self.play(
            FadeIn(r_line),
            FadeIn(arrow_r)
        )

        # Save the state of camera
        frame.save_state()

        self.play(
            frame.increment_phi, 20 * DEGREES,
        )

        self.play(
            FadeIn(dis_text),
        )

        self.play(
            frame.increment_phi, -10 * DEGREES,
        )
        self.wait(3)

        self.play(
            FadeTransform(dis_text, r),
        )

        self.wait(3)

        self.play(
            FadeIn(dv_shell),
            FadeIn(arrow_dv_shell)
        )

        self.wait(3)

        dr_line = Line(
            [-0.3, 0.22, math.e ** (- 0.3 ** 2)],
            [-0.2, 0, math.e ** (- 0.3 ** 2)],
        ).set_color(BLACK)

        arrow_dr = Arrow(
            [-0.5, 0, 1.4],
            [-0.25, 0.05, 0.7]
        ).set_color(BLACK)

        self.play(
            FadeIn(dr_line),
            FadeIn(arrow_dr),
            FadeIn(dr),
        )
        self.wait(3)

        dr_instruct = Tex("\\implies dr \\rightarrow 0").next_to(instruct_text2, RIGHT)
        dr_instruct.set_color(BLUE).fix_in_frame()

        self.play(
            FadeIn(dr_instruct)
        )

        self.wait(3)

        self.play(
            dv_shell.animate.shift(1.8 * LEFT + 0.3 * UP),
            dr.animate.shift(2 * LEFT + 0.3 * UP),
            r.animate.shift(2.0 * LEFT + 0.3 * UP),
            surface_tex.animate.shift(2 * LEFT),
            self.camera.frame.move_to, np.array((-1., -1., 0.)),
        )
        self.wait(3)

        shell_equ = Tex("V = sh = \\int_{0}^{\\infty} e^{-r^2}2 \\pi r dr", isolate=["s", "h", "e^{-r^2}", "2 \\pi r dr"])
        shell_equ.to_corner(UR).fix_in_frame()
        shell_equ.set_color_by_tex("s", BLUE)
        shell_equ.set_color_by_tex("h", GREEN)

        shell_equ.set_color_by_tex("2 \\pi r dr", BLUE)
        shell_equ.set_color_by_tex("e^{-r^2}", GREEN)

        shell_equ2 = Tex("=\\pi \\int_{-\\infty}^{0} e^{-r^2} d(-r^2)").next_to(shell_equ, DOWN).fix_in_frame()
        shell_equ3 = Tex("=\\pi e^{-r^2} \\bigg|_{-\\infty}^{0} = \\pi").next_to(shell_equ2, DOWN).fix_in_frame()
        shell_equ3.set_color_by_tex("\\pi", RED)
        shell_equ3.shift(0.4 * LEFT)

        self.play(
            FadeIn(shell_equ),
        )
        self.wait(3)
        
        self.play(
            TransformMatchingTex(shell_equ.copy(), shell_equ2),
        )

        self.wait(3)

        self.play(
            TransformMatchingTex(shell_equ2.copy(), shell_equ3),
        )

class ApproximateCircle(Scene):
    """ApproximateCircle Scene for the video.
       1. Introduce the idea of area calculation 
       2. Show the related animations
    """
    CONFIG = {
        'radius': 1.5,
        "dR" : 0.1,
        "stroke_color" : WHITE,
        "fill_color" : BLUE_E,
        "fill_opacity" : 1.,
        "ring_colors" : [BLUE, GREEN],
        "dR_color" : YELLOW,
        "unwrapped_tip" : 2*RIGHT+0.5*UP,
        "radial_line_color" : MAROON_B,
    }

    def construct(self):
        # prepare the circle first
        self.prepare_circle()
        # then split the circle into rings
        self.slice_rings()
        # show dr now
        self.show_dr()
        # make the ring approximate as the rectangle  
        self.straighten_ring()

    def prepare_circle(self):
        self.circle = Circle(
            radius = self.radius,
            stroke_color = self.stroke_color,
        )
        self.circle.to_corner(UL)
        intro_text = Tex("\\text{The area of a }", "\\text{circle}", "?").next_to(self.circle, 0.1 * UP + 5 * RIGHT)
        intro_text.set_color_by_tex('circle', GREEN)

        radius_line = Line(
            self.circle.get_center(),
            self.circle.get_right(),
            color = self.radial_line_color
        ).set_color(BLUE)

        radius_brace = Brace(radius_line, buff = SMALL_BUFF).set_color(BLUE)
        radius_label = Tex('R').set_color(WHITE).next_to(radius_brace, DOWN)

        radius_group = VGroup(
            radius_line, radius_brace, radius_label
        )
        self.play(
            ShowCreation(self.circle),
            FadeIn(intro_text),
            ShowCreation(radius_group)
        )
        self.wait(3)

        area_equ = Tex("s = \\pi R^2").next_to(intro_text, 3 * DOWN)

        self.play(
            FadeIn(area_equ)
        )
        self.wait(3)

        intro_text_2 = Tex("\\text{But Why?}").next_to(area_equ, 3 * DOWN)

        self.play(
            FadeIn(intro_text_2)
        )
        self.wait(3)
        fadeGroup = VGroup(
            intro_text, intro_text_2, area_equ, radius_group
        )

        self.wait(3)
        self.play(
            FadeOut(fadeGroup)
        )
        self.wait(3)
 
    def slice_rings(self):
        rings = self.get_rings()
        self.rings = rings
        self.ring = rings[3].copy()
        rings.set_stroke(BLACK, width=1)

    def get_rings(self, **kwargs):
        dR = kwargs.get("dR", self.dR)
        colors = kwargs.get("colors", self.ring_colors)
        radii = np.arange(0, self.radius, dR)
        colors = color_gradient(colors, len(radii))

        # taking color overlapping into consideration
        # we set color from outside to inside
        rings = VGroup(*[
            self.get_ring(radius, dR=dR, color=color)
            for radius, color in zip(radii[-1: :-1], colors[-1: :-1])
        ])
        rings.to_corner(UL)
        return rings

    def get_ring(self, radius, dR, color):
        ring = Circle(radius=radius+dR).center()
        inner_ring = Circle(radius=radius)
        inner_ring.rotate(np.pi, RIGHT)
        # add the points of inner_ring
        ring.append_vectorized_mobject(inner_ring)
        ring.set_stroke(width=0)
        ring.set_fill(color, opacity=self.fill_opacity)
        ring.move_to(self.circle)
        ring.R = radius
        ring.dR = dR
        return ring

    def show_dr(self):
        radius = Line(
            self.circle.get_center(), 
            np.array([-5.66, 2.9526, 0]),
        )
        r_label = Tex("r")
        r_label.next_to(radius.get_center(), UP+RIGHT, SMALL_BUFF)
        self.ring_radius_group = VGroup(radius, r_label)
        self.ring_radius_group.set_color(BLACK)

        radius_line = Line(
            self.circle.get_center(),
            self.circle.get_right(),
            color = self.radial_line_color
        ).set_color(BLUE)

        radius_brace = Brace(radius_line, buff = SMALL_BUFF).set_color(BLUE)
        radius_label = Tex('R').set_color(BLACK).next_to(radius_brace, DOWN)

        radius_group = VGroup(
            radius_line, radius_brace, radius_label
        )
 
        alt_side_brace = Brace(self.rings[-1], UP).set_color(RED)
        alt_side_brace.stretch(0.5, 0)
        alt_side_brace.shift(1.15*RIGHT + 0.25*DOWN)
        alt_brace_label = Tex(r"\mathrm{dr}").set_color(BLACK)
        alt_brace_label.next_to(alt_side_brace, UP)
        self.alt_barce_label = alt_brace_label

        alt_group = VGroup(alt_side_brace, alt_brace_label)
        frame = self.camera.frame
        frame.save_state()

        # Zoom in
        self.play(
            frame.set_width, self.rings.get_width()*3.0,
            # Move the camera to the object
            frame.move_to, self.rings,
        )

        self.wait(3)
        tip = TexText("Split the circle into rings").next_to(self.circle, UP)
        tip2 = TexText("The area of the outer ring?").next_to(self.circle, UP)
        self.play(
            FadeIn(tip),
            FadeIn(
                self.rings,
                lag_ratio = 0.5,
                run_time = 3,
            ),
        )

        self.wait(3)
        self.play(
            self.rings[4:].animate.set_color(YELLOW)
        )

        self.wait(3)
        self.play(
            FadeTransform(tip, tip2),
            ShowCreation(radius_group),
            ShowCreation(self.ring_radius_group),
            ShowCreation(alt_group),
            run_time = 3,
        )
        self.wait(3)

        # restore the frame
        self.play(
            Restore(frame),
            FadeOut(tip2),
        )
        self.wait(3)

    def straighten_ring(self):
        # unwrap the rings and straighten
        self.unwrap_rings(self.ring, to_edge = RIGHT)
        top_brace, side_brace = [
            Brace(
                self.ring, vect, buff = SMALL_BUFF,
                min_num_quads = 2,
            )
            for vect in (UP, LEFT)
        ]
        # focus on the upper line
        top_brace.scale(self.ring.R/(self.ring.R+self.dR))
        side_brace.set_stroke(WHITE, 0.5)

        width_label = Tex("2 \\pi r", isolate=['\\pi', 'r']).set_color(GREEN)
        width_label.next_to(top_brace, UP, SMALL_BUFF)
        dr_label = Tex("dr").set_color(BLUE)
        dr_label.next_to(side_brace, LEFT, SMALL_BUFF)
        dr_label.save_state()

        self.play(GrowFromCenter(top_brace))
        self.wait(3)
        self.play(
            Write(width_label.get_part_by_tex('\\pi')),
            ReplacementTransform(
                self.ring_radius_group[1].copy(),
                width_label
            )
        )

        self.wait(3)
        self.play(
            GrowFromCenter(side_brace),
            TransformMatchingTex(self.alt_barce_label.copy(), dr_label)
        )
        self.wait(3)

        rect = Rectangle(6.9117, 0.05).set_fill(GREEN, 1.).set_stroke(RED, opacity=0.)
        rect.move_to(self.unwrapped)

        new_side_brace = Brace(
            rect, LEFT, buff = SMALL_BUFF,
            min_num_quads = 2,
        )
 
        self.area_q = Tex("\\text{Area} \\approx ?", isolate=['\\text{Area}', '\\approx', '?'])

        self.area_q.next_to(width_label, 2 * UP + 4 * LEFT)
        self.add(self.area_q)
        self.wait(3)

        new_dr_label = Tex("dr").set_color(BLUE)
        new_dr_label.next_to(new_side_brace, LEFT, SMALL_BUFF)
        instruct_dr = Tex("dr \\rightarrow 0")
        instruct_dr.next_to(width_label, 2 * UP + 4 * RIGHT)
        self.add(instruct_dr)
        self.wait(3)

        rect_text = Tex("\\text{Rectangle").next_to(instruct_dr, 3 * LEFT)

        self.play(
            FadeTransform(self.unwrapped, rect),
            FadeTransform(side_brace, new_side_brace),
            FadeTransform(dr_label, new_dr_label),
            ReplacementTransform(self.area_q.get_part_by_tex('?'), rect_text)
        )

        self.wait(3)
        formula = Tex("s = 2 \\pi r dr", isolate=['dr', '\\pi', 'r']).next_to(rect, 2 * DOWN).set_color(GREEN)
        formula.set_color_by_tex('dr', BLUE)

        self.play(
            FadeTransform(new_dr_label.copy(), formula.get_part_by_tex('dr')),
            TransformMatchingTex(width_label.copy(), formula)
        )

        self.wait(3)
        inte_instruct = TexText("Integration over rings").next_to(self.circle, 4 * DOWN + 0.8 * RIGHT)

        inte_formula = Tex("\\implies \\int_{0} ^ R 2\\pi r dr = \\pi R^2").next_to(inte_instruct, 4 * RIGHT)

        self.play(
            Write(inte_instruct),
            Write(inte_formula)
        )

        self.wait(3)

    def unwrap_rings(self, *rings, **kwargs):
        rings = VGroup(*rings)
        self.unwrapped = VGroup(*[
            self.get_unwrapped(ring, **kwargs)
            for ring in rings
        ])
        inner_part = self.rings[4:].copy()
        new_rings = VGroup(rings, inner_part)
        self.play(
            new_rings.rotate, np.pi/2,
            new_rings.next_to, self.unwrapped.get_top(), 1. * UP,
            run_time = 2,
            path_arc = np.pi/2,
        )
        straighten_text = Tex("\\text{Straighten the ring}").next_to(self.unwrapped, 8 * UP)
        self.play(
            Write(straighten_text),
            ReplacementTransform(rings, self.unwrapped, run_time = 3),
            FadeOut(inner_part, run_time=3)
        )
        self.wait(3)
       
    def get_unwrapped(self, ring, to_edge = LEFT):
        R = ring.R
        R_plus_dr = ring.R + ring.dR
        n_anchors = ring.get_num_curves()
        result = VMobject()
        result.set_points_as_corners([
            interpolate(np.pi*R_plus_dr*LEFT,  np.pi*R_plus_dr*RIGHT, a)
            for a in np.linspace(0, 1, n_anchors//2)
        ]+[
            interpolate(np.pi*R*RIGHT+ring.dR*UP,  np.pi*R*LEFT+ring.dR*UP, a)
            for a in np.linspace(0, 1, n_anchors//2)
        ])
        result.set_style(
            stroke_color = ring.get_stroke_color(),
            stroke_width = ring.get_stroke_width(),
            fill_color = ring.get_fill_color(),
            fill_opacity = ring.get_fill_opacity(),
        )
        result.move_to(self.unwrapped_tip, aligned_edge = UP)
        # in the upper screen
        result.shift(R_plus_dr*0.7*UP)
        if to_edge is not None:
            result.to_edge(to_edge)

        return result
 
class Summary(Scene):
    """Summary Scene for the video."""
    def construct(self):
        # now comes the summary
        title = Tex("\\text{Summary}").to_corner(UL)
        disk_res = Tex("\\text{Disk Method: } V = Q ^ 2")
        cylinder_res = Tex("\\text{Cylinder Method: } V = \\pi")
        final_imply = Tex("\\implies Q = \\int_{-\\infty}^{\\infty} e^{-x^2} \\mathrm{dx} = \\sqrt{\\pi}")
        final_imply_ = Tex("Q = \\int_{-\\infty}^{\\infty} e^{-x^2} \\mathrm{dx} = \\sqrt{\\pi}", isolate=["\\sqrt{\\pi}"])

        final_imply_.set_color_by_tex("\\sqrt{\\pi}", BLUE)

        statistic_text = Tex("\\text{Connection with statistics}").to_corner(UL)

        self.play(
            FadeIn(title)
        )
        self.wait(3)

        self.play(
            FadeIn(disk_res)
        )

        self.wait(3)
        self.play(
            disk_res.animate.shift(UP),
            FadeIn(cylinder_res)
        )
        self.wait(3)

        self.play(
            disk_res.animate.shift(UP),
            cylinder_res.animate.shift(UP),
            FadeIn(final_imply)
        )
        self.wait(3)

        self.play(
            FadeOut(disk_res),
            FadeOut(cylinder_res),
            FadeOut(final_imply),
            final_imply_.animate.shift(2.3 * UP),
            FadeTransform(title, statistic_text)
        )
        self.wait(3)

        statistic_equ1 = Tex(r"\implies \ \frac{1}{\sqrt{\pi}} \int_{-\infty}^{\infty} e^{-x^2} \mathrm{dx} = 1", isolate=[r"\frac{1}{\sqrt{\pi}}"])
        statistic_equ1.next_to(final_imply_, DOWN)
        statistic_equ1.set_color_by_tex(r"\frac{1}{\sqrt{\pi}}", BLUE)
        
        statistic_equ2 = Tex(r"\implies \ \frac{1}{\sqrt{\pi}} \int_{-\infty}^{\infty} e^{-(x/\sqrt{2}\sigma)^2} \mathrm{d (\frac{x}{\sqrt{2}\sigma})} = 1",
                     isolate=[r"e^{-(x/\sqrt{2}\sigma)^2}", r"\mathrm{d (\frac{x}{\sqrt{2}\sigma})}"])

        statistic_equ2.set_color_by_tex(r"e^{-(x/\sqrt{2}\sigma)^2}", GREEN)
        statistic_equ2.set_color_by_tex(r"\mathrm{d (\frac{x}{\sqrt{2}\sigma})}", GREEN)

        statistic_equ2.next_to(statistic_equ1, DOWN)

        rescaled_rect = Rectangle(1.2, 0.6).set_color(GREEN).shift(0.3 * DOWN + 0.3 * RIGHT)
        rescaled_rect2 = Rectangle(1.0, 1.2).set_color(GREEN).shift(0.5 * DOWN + 2.2 * RIGHT)

        rescaled_text = Tex("\\text{Rescale x}").next_to(statistic_equ2, UR).set_color(GREEN)
        arrow1 = Arrow(
            rescaled_text.get_left(),
            rescaled_rect.get_top()
        ).set_color(YELLOW)

        arrow2 = Arrow(
            rescaled_text.get_left(),
            rescaled_rect2.get_right()
        ).set_color(YELLOW)

        statistic_equ3 = Tex(r"\implies \ \frac{1}{\sqrt{2\pi}\sigma} \int_{-\infty}^{\infty} e^{-x^2/ 2\sigma^2} \mathrm{dx} = 1", isolate=[r"\frac{1}{\sqrt{2\pi}\sigma}"])
        statistic_equ3.set_color_by_tex(r"\frac{1}{\sqrt{2\pi}\sigma}", BLUE)
        statistic_equ3.next_to(statistic_equ2, DOWN)

        self.play(
            TransformMatchingTex(final_imply_.copy(), statistic_equ1)
        )
        self.wait(3)


        self.play(
            TransformMatchingTex(statistic_equ1.copy(), statistic_equ2)
        )
        self.wait(3)


        self.play(
            FadeIn(rescaled_rect),
            FadeIn(rescaled_rect2),
            ShowCreation(rescaled_text),
            ShowCreation(arrow1),
            ShowCreation(arrow2),
        )

        self.wait(3)

        self.play(
            TransformMatchingTex(statistic_equ2.copy(), statistic_equ3)
        )

        self.wait(3)

        rect_normal = Rectangle(6.0, 1.5).set_color(RED)
        statistic_equ4 = Tex(r"\frac{1}{\sqrt{2\pi}\sigma} \int_{-\infty}^{\infty} e^{-x^2/ 2\sigma^2} \mathrm{dx} = 1")

        statistic_equ2_group = VGroup(
            statistic_equ2, arrow1, arrow2, rescaled_text, rescaled_rect, rescaled_rect2
        )

        self.play(
            FadeOut(final_imply_),
            FadeOut(statistic_equ1),
            FadeOut(statistic_equ2_group),
            FadeOut(statistic_equ3),
            FadeIn(statistic_equ4)
        )

        self.wait(3)
        normal_des = Tex("\\text{Normal Distribution}").set_color(BLUE).next_to(statistic_equ4, 6 * UP)
        normal_arrow = Arrow(
            normal_des.get_bottom(),
            rect_normal.get_top()
        ).set_color(YELLOW)

        self.play(
            ShowCreation(rect_normal),
            ShowCreation(normal_arrow),
            ShowCreation(normal_des),
        )

class Acknowledgement(Scene):
    """Acknowledgement Scene for the video.
       1. David Jerison for the idea 
       2. Grant Sanderson for the manim
    """
    def construct(self):
        title = Tex("\\text{Acknowledgement}").to_corner(UL)
        self.play(
            FadeIn(title)
        )
        self.save_state()

        jerison = ImageMobject("/home/tony/有趣项目/manim-projects/prior/jerison.jpeg").next_to(title, 2 * DOWN)
        intro_jerison1 = Tex("\\text{David Jerison}").shift(3 * UP)
        intro_jerison2 = Tex("\\rightarrow \\text{Professor of Mathematics, MIT}").shift(2.6 * RIGHT + 2 * UP)
        intro_jerison3_1 = Tex("\\rightarrow \\text{Main Interests: }").shift(1 * UP)
        intro_jerison3_1.align_to(intro_jerison2, np.array((-0.9657, 0., 0.)))
        intro_jerison3_2 = Tex("\\text{Fourier analysis}").shift(1.7 * RIGHT)
        intro_jerison3_3 = Tex("\\text{Partial differential equations}").shift(DOWN + 3 * RIGHT)
        intro_jerison3_3.align_to(intro_jerison3_2, np.array((-2.6174, 0., 0.)))

        intro_jerison4_1 = Tex("\\rightarrow \\text{Teaching: }").shift(2 * DOWN)
        intro_jerison4_1.align_to(intro_jerison3_1, np.array((-0.9657, 0., 0.)))
        intro_jerison4_2 = Tex("18.01, 18.02, 18.03", isolate=["18.01"]).shift(3 * DOWN)
        intro_jerison4_2.align_to(intro_jerison3_2, np.array((-0.2785, 0., 0.)))

        intro_jerison4_2.set_color_by_tex("18.01", BLUE)

        self.play(
            FadeIn(jerison),
            Write(intro_jerison1)
        )
        self.wait()

        self.play(
            FadeIn(intro_jerison2)
        )

        self.wait()

        self.play(
            FadeIn(intro_jerison3_1),
            FadeIn(intro_jerison3_2),
            FadeIn(intro_jerison3_3),
        )
        self.wait()

        self.play(
            FadeIn(intro_jerison4_1),
            FadeIn(intro_jerison4_2),
        )

        self.embed()
        self.restore()

        grant = ImageMobject("/home/tony/有趣项目/manim-projects/prior/grant.jpeg").next_to(title, 2 * DOWN)
        intro_grant1 = Tex("\\text{Grant Sanderson}").shift(3 * UP)
        intro_grant2 = Tex("\\rightarrow \\text{Owner of 3Blue1Brown}").shift(2 * UP + 1.0 * RIGHT)
        intro_grant3 = Tex("\\rightarrow \\text{Creator of Manim}", isolate=["Manim"]).shift(0.3 * UP)
        intro_grant3.align_to(intro_grant2, np.array((-1.6744, 0., 0.)))
        intro_grant3.set_color_by_tex("Manim", BLUE)

        intro_grant4 = Tex("\\rightarrow \\text{Producer of fun videos}").shift(1.5 * DOWN)
        intro_grant4.align_to(intro_grant3, np.array((-1.6744, 0., 0.)))

        self.play(
            FadeIn(grant),
            Write(intro_grant1)
        )
        self.wait()

        self.play(
            FadeIn(intro_grant2)
        )

        self.wait()

        self.play(
            FadeIn(intro_grant3),
        )
        self.wait()

        self.play(
            FadeIn(intro_grant4),
        )

class Ending(Scene):
    """Ending Scene for the video."""
    def construct(self):

        thank = TexText("Thanks!")
        author = TexText("By Yunpengtai")
        self.play(
            FadeIn(thank)
        )

        self.play(
            thank.animate.shift(UP),
            Write(author),
        )
        self.wait(3)
