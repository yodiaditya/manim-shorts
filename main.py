"""
MIT License

Copyright (c) 2025 Yodi aditya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from manim import *

# Configure resolution and frame rate
width, height = 1080, 1920
config.frame_size = [width, height]
config.frame_rate = 60

class Main(Scene):

    def wrapText(self, text, max_width):
        """
        Manually wraps text to fit within the specified max_width.
        """
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            # Check if adding the word exceeds max_width
            if Text(current_line + " " + word).width <= max_width:
                current_line += " " + word
            else:
                lines.append(current_line.strip())
                current_line = word

        # Add the final line
        lines.append(current_line.strip())
        return lines

    def writeText(self, long_text, font_size=80):
        # Wrap the text manually
        max_width = config.frame_width - 1  # Subtract a small margin
        wrapped_lines = self.wrapText(long_text, max_width)

        # Create Text objects for each line
        text_objects = [Text(line, font_size=font_size) for line in wrapped_lines]

        # Arrange the lines in a VGroup with custom spacing
        text_group = VGroup(*text_objects).arrange(DOWN, buff=0.5)

        # Center the text group on the screen
        text_group.move_to(ORIGIN)

        return text_group

    def createArray(self, curA, with_index=False):
        v = VGroup(
            *[
                VGroup(
                    Square(side_length=2.5, color=WHITE, stroke_width=12),
                    Text(str(x), font_size=60),
                    Text(str(i), font_size=20)
                )
                for i,x in enumerate(curA)
            ])

        for i in range(len(v)):
            if i%2: col = BLUE 
            else: col = RED
            v[i].set_color(col)

        v.arrange(RIGHT, buff=0.3)

        for i in range(len(v)):
            v[i][2].move_to(v[i][1].get_bottom()+DOWN*.35)

        return v

    def construct(self):
        RUN_TIME = 0.22 
        Text.set_default(font_size=80, font="Noto Sans")

        text=Text("Two Sum Pair\n\nArray Problems")

        self.play(Write(text), run_time=RUN_TIME)
        self.wait(2)
        self.play(Unwrite(text), run_time=RUN_TIME*2)
    
        text = self.writeText('Given an array and target (all integers) return "indices" of the "two numbers" equal target.')
        self.play(Write(text), run_time=RUN_TIME)
        self.wait(3)
        self.play(Unwrite(text), run_time=RUN_TIME*2)

        def createExamples(input, target, output, description):    
            text = Text("Input").move_to(UP*11)
            input = self.createArray(input).move_to(UP*9)

            text2 = Text("Target").move_to(UP*6)
            target = self.createArray(target).move_to(UP*4)

            text3 = Text("Output").move_to(UP*1)
            output = self.createArray(output).move_to(DOWN*1)

            text_description = self.writeText(description).move_to(DOWN*5)

            self.play(Write(text_description), Write(text), Write(text2), Write(text3), Create(input), Create(target), Create(output))
            self.wait(3)
            self.play(
                *[FadeOut(mob)for mob in self.mobjects]
            )

        createExamples([2,7,11,15], [9], [0,1], "Given input [2,7,11,15], target is 9, result is [0,1]")
        createExamples([3,2,4],[6],[1,2], "Given input [3,2,4], target is 6, result is [1,2]")
        createExamples([3,3],[6],[0,1], "Given input [3,3], target is 6, result is [0,1]")

        text=Text("Approach 1: Brute Force")
        self.play(Write(text), run_time=RUN_TIME)
        self.wait(1)
        self.play(Unwrite(text), run_time=RUN_TIME*2)

        img = ImageMobject("assets/img1.png").scale(1.8).move_to(UP*4)
        self.add(img)

        text = self.writeText("Iterate the array and compare i position to next i + 1").move_to(DOWN*5)
        self.play(Write(text),run_time=RUN_TIME)
        self.wait(3)
        self.play(Unwrite(text), run_time=RUN_TIME*2)

        text=Text("Time complexity: O(n * n)").move_to(DOWN*5)
        self.play(Write(text), run_time=RUN_TIME)
        self.wait(1)
        self.play(Unwrite(text), run_time=RUN_TIME*2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        text = self.writeText('Solution: Hashmap and remaining result from target minus current array value')
        self.play(Write(text), run_time=RUN_TIME)
        self.wait(3)
        self.play(Unwrite(text), run_time=RUN_TIME*2)
 
        img = ImageMobject("assets/img2.png").scale(1.8).move_to(UP*4)
        self.add(img)

        # Wait for a moment
        self.wait(1)

         # Define screen width and text line height
        screen_width = config.frame_width  # Total width of the screen

        # Create a rectangle with 90% screen width and 3 lines of height
        rectangle = Rectangle(
            width=screen_width * 0.9,
            height=0.05,
            color=YELLOW,
            fill_opacity=0.7,  # Semi-transparent
            stroke_width=0  # Border thickness
        )

        def createWalkthrough(text, cursor_position):
            # Position the rectangle at the top of the screen
            rectangle.move_to(cursor_position)

            # Add rectangle to the scene
            self.add(rectangle)

            text = self.writeText(text).move_to(DOWN*5)
            self.play(Write(text),run_time=RUN_TIME)
            self.wait(2)
            self.play(Unwrite(text), run_time=RUN_TIME*2)

            self.remove(rectangle)

        createWalkthrough("Step 1: Create an Hashmap", UP * 6.1)
        createWalkthrough("Step 2: Iterate Array", UP * 5)
        createWalkthrough("Step 3: Calculate the remaining", UP * 4.5)
        createWalkthrough("Step 4: Check if in Hashmap exists", UP * 3.3)
        createWalkthrough("Step 5: If not found, add into Hashmap", UP * 1.7)

        text = self.writeText('Solution for Two Sum is using Hashmap and Remaining from Target').move_to(DOWN*4)
        self.play(Write(text), run_time=RUN_TIME)
        self.wait(3)
        self.play(Unwrite(text), run_time=RUN_TIME*2)