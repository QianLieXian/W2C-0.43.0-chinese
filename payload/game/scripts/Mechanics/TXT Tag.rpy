# Kinetic Text Tags Ren'Py Module
# 2021 Daniel Westfall <SoDaRa2595@gmail.com>

# http://twitter.com/sodara9
# I'd appreciate being given credit if you do end up using it! :D Would really
# make my day to know I helped some people out!
# Really hope this can help the community create some really neat ways to spice
# up their dialogue!
# http://opensource.org/licenses/mit-license.php
# Github: https://github.com/SoDaRa/Kinetic-Text-Tags
# itch.io: https://wattson.itch.io/kinetic-text-tags
# Forum Post: https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=60527&sid=75b4eb1aa5212a33cbfe9b0354e5376b

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### UPDATE ###
# With the new ATL text tag, a handful of effects I've made have become redundant.
# Namely the bounce (bt), fadein (fi) and rotation (rotat) effects.
# However, I'll leave them in here for posterity and in case someone would like
# to reuse some of the code for whatever purpose.
# Plus the bounce and fadein may be faster to type for some. And I'd probably
# break some code if I did. Though feel free to remove them if you find them
# to be clutter.
# General Notes:
 # I have not tested every transform property and such some may not work as indended
    # Most common ones work fine such as pos and offset.
    # I can't imagine this being an issue for most of them. However I imagine that
    # anchor, xanchor, yanchor, fit and events may not have the indended effect.

 # Tranforms used for ATLText must take up time if they repeat
    # The following will cause an error:
    # transform random_pos(range):
    #     xpos (random.random() * range)
    #     ypos (random.random() * range)
    #     # If there were a pause 0.01 here, it'd be fine. w/o it, renpy flags this as an infinite loop.
    #     repeat

 # Sadly, repeating a section a limited number of times does not work.
    # As an example:
    # transform text_rotate_3d(time=1.5):
    #     matrixanchor (0.5,0.5)
    #     matrixtransform RotateMatrix(0,0,0) * OffsetMatrix(0,0,100)
    #     linear time matrixtransform RotateMatrix(180,0,180) * OffsetMatrix(0,0,100)
    #     linear time matrixtransform RotateMatrix(360,0,360) * OffsetMatrix(0,0,100)
    #     matrixtransform RotateMatrix(0,0,0) * OffsetMatrix(0,0,100)
    #     repeat 3
    #     matrixtransform RotateMatrix(0,0,0) * OffsetMatrix(0,0,100)
    #     linear time matrixtransform RotateMatrix(180,0,180) * OffsetMatrix(0,0,50)
    #     linear time matrixtransform RotateMatrix(360,0,360) * OffsetMatrix(0,0,0)
    # The 'repeat 3' will be skipped and instead just fall through into the next section.
    # Thus, repeated sections must be included manually. Which sucks but idk a way
    # around it right now.
    # Thankfully, infinite repeats work without issue.

 # Using matrixtransform and zpos is possible. However, standard text is applied on
    # the screens layer. Using:
    # camera screens:
    #     perspective True
    # Will enable that layer to use the 3D stage.
    # HOWEVER!!!
    # Doing so will prevent the user from being able to interact with any buttons
    # on that layer. Therefore, it is advised that if you want to use the 3D stage
    # for text transforms, you have it be handled on a layer.
    # Below is an example of how to implement this.

# While making this I frequently had the source code up for things
  # Relevant bits to look over were:
  # defaultstore.rpy for how At() works
  # display/motion.py for how various kinda of movement are handled
  # display/transform.py for the TransformState, Tranform and ATLTransform classes
  # atl.py for ATLTransformBase class, which handles a lot of functions for ATLTransform
  # display/accelerator.pyx for how Tranform handles rendering.

transform bounce:
    ease 0.5 yoffset 10 matrixcolor TintMatrix("#f00")
    ease 0.5 yoffset -10 matrixcolor TintMatrix("#00f")
    repeat

transform bounce_text(yoff):
    ease 0.5 ypos yoff
    ease 0.5 ypos -yoff
    repeat

transform rotate_text(speed):
    linear speed rotate 180
    linear speed rotate 360
    rotate 0
    repeat

transform drop_text(letter, time):
    contains:
        letter
    contains:
        letter
        yoffset 0 alpha 1
        easeout_circ time yoffset 10 alpha 0
        letter
        repeat

transform fade_in_text(time=0.5, distance=20):
    alpha 0 xoffset distance
    ease time alpha 1 xoffset 0

# Doing the following will help with using 3D stage transforms on say screen text
  # Defining the new layer below the screens layer to allow it to go behind anything on the screens layer
# define config.layers = [ 'master', 'transient', 'threeD_text', 'screens', 'overlay' ]
  # Tell the character to use our new layer to display the screen.
# define e_3d = Character("Eileen3D", show_layer="threeD_text")
  # And before using the character, be sure to do:
  # camera threeD_text:
  #     perspective True
  # And the 3D stage things should work.
  # You can also make this layer the default for showing the say screen by doing.
  # define config.say_layer = "threeD_text"
  # Also remember you can override elements of a character for a line, such as with:
    # "Here's a narration line with an override to {atl=-0.1, text_rotate_3d}allow for 3D Text.{/atl}" (show_layer="threeD_text")

transform text_rotate_3d(time=1.5):
    matrixanchor (0.5,0.5)
    matrixtransform RotateMatrix(0,0,0) * OffsetMatrix(0,0,100)
    linear time matrixtransform RotateMatrix(180,0,0) * OffsetMatrix(0,0,100)
    linear time matrixtransform RotateMatrix(360,0,0) * OffsetMatrix(0,0,100)
    matrixtransform RotateMatrix(0,0,0) * OffsetMatrix(0,0,100)
    repeat
    
##### Our preference to disable the chaos text #####
default preferences.chaos_on = False  # You can change this to be gui.chaos_text or persistent.chaos_text if you'd prefer.

init 1 python:
    import random
    import math

    # This will maintain what styles we want to apply and help us apply them
    class DispTextStyle():
        # Notes:
        #   - "" denotes a style tag. Since it's usually {=user_style} and we partition
        #     it over the '=', it ends up being an empty string
        #   - If you want to add your own tags to the list, I recommend adding them
        #     before the ""
        #   - Self-closing tags should not be added here and should be handled
        #     in the text tag function.
        custom_tags = ["lg", "omega", "bt", "fi", "sc", "rotat", "chaos", "move"]
        accepted_tags = ["", "b", "s", "u", "i", "color", "alpha", "font",  "size", "outlinecolor", "plain", 'cps']
        custom_cancel_tags = ["/" + tag for tag in custom_tags]
        cancel_tags = ["/" + tag for tag in accepted_tags]
        def __init__(self):
            self.tags = {}

        # For setting style properties. Returns false if it accepted none of the tags
        def add_tags(self, char):
            tag, _, value = char.partition("=") # Separate the tag and its info
            # Add tag to dictionary if we accept it
            if tag in self.accepted_tags or tag in self.custom_tags:
                if value == "":
                    self.tags[tag] = True
                else:
                    self.tags[tag] = value
                return True
            # Remove mark tag as cleared if should no longer apply it
            if tag in self.cancel_tags or tag in self.custom_cancel_tags:
                tag = tag.replace("/", "")
                self.tags.pop(tag)
                return True
            return False # If we got any other tag, tell the function to let it pass

        # Applies all style properties to the string
        def apply_style(self, char):
            new_string = ""
            # Go through and apply all the tags
            new_string += self.start_tags()
            # Add the character in the middle
            new_string += char
            # Now close all the tags we opened
            new_string += self.end_tags()
            return new_string

        # Spits out start tags. Primarily used for SwapText
        def start_tags(self):
            new_string = ""
            # Go through the custom tags
            for tag in self.custom_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            # Go through the standard tags
            for tag in self.accepted_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            return new_string

        # Spits out ending tags. Primarily used for SwapText
        def end_tags(self):
            new_string = ""
            # The only tags we are required to end are any custom text tags.
            # And should also end them in the reverse order they were applied.
            reversed_cancels = [tag for tag in self.custom_cancel_tags]
            reversed_cancels.reverse()
            for tag in reversed_cancels:
                temp = tag.replace("/", "")
                if temp in self.tags:
                    new_string += "{" + tag + "}"
            return new_string


    ### TEXT WRAPPER CLASSES ###
    # Basic text displacement demonstration
    class BounceText(renpy.Displayable):
        def __init__(self, child, char_offset, amp=20, period=4.0, speed = 1.0, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(BounceText, self).__init__(**kwargs) # REMEMBER TO RENAME HERE TO YOUR CLASS

            # For all of my classes, I assume I am being passed a displayable
            # of class Text. If you might not, I recommend going with the default of
            # self.child = renpy.displayable(child)
            self.child = child
            self.amp = amp # The amplitude of the sine wave
            self.char_offset = char_offset # The offset into the sine wave
            self.period = period # Affects the distance between peaks in the wave.
            self.speed = speed   # Affects how fast our wave moves as a function of time.

        def render(self, width, height, st, at):
            if preferences.enable_TXT_Tag == False: 
                return renpy.render(self.child, width, height, st, at)
            # Where the current offset is calculated
            # (self.char_offset * -.1) makes it look like the left side is leading
            # We use st to allow this to change over time
            curr_height = math.sin(self.period*((st * self.speed)+(float(self.char_offset) * -.1))) * float(self.amp)

            ####  A Transform can be used for several effects   ####
            # t = Transform(child=self.child,  alpha = curr_height)

            # Create a render from the child.
            # Replace self.child with t to include an alpha or zoom transform
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # This will position our child's render. Replacing our need for an offset Transform
            render.subpixel_blit(child_render, (0, curr_height))

            renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

    # Simple fade in. Helps show some ideas for timing
    # May want to modify to allow it to skip to the end if the user clicks.
    # Otherwise plays for the full time given.
    class FadeInText(renpy.Displayable):
        def __init__(self, child, char_num, fade_time, slide_distance=100, **kwargs):
            super(FadeInText, self).__init__(**kwargs)

            # The child.
            self.child = child
            self.fade_time = fade_time
            self.display_time = .01
            self.slide_distance = slide_distance
            # This is to get seconds per character on screen for later
            # Allowing this effect to scale with the player's desired text speed
            cps = 0.0
            if preferences.text_cps != 0: # Avoid division by 0.0
                cps = (1.0 / preferences.text_cps)
            self.time_offset = char_num * cps  # How long to wait before doing things

        def render(self, width, height, st, at):
            if preferences.enable_TXT_Tag == False: 
                return renpy.render(self.child, width, height, st, at)
            curr_alpha = 0.0
            xoff = 5.0
            if st > self.time_offset:
                adjust_st = st - self.time_offset # Adjust for time delay
                curr_alpha = adjust_st/self.fade_time
                xoff = max(self.slide_distance - ((adjust_st/self.fade_time) * self.slide_distance), 0)
            # Example of using transform to adjust alpha
            t = Transform(child=self.child,  alpha = curr_alpha)
            child_render = renpy.render(t, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (xoff, 0))
            # Stop redrawing when the animation is finished.
            if st <= self.fade_time + self.time_offset:
                renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # Simple random motion effect
    class ScareText(renpy.Displayable):
        def __init__(self, child, square=2, **kwargs):
            super(ScareText, self).__init__(**kwargs)

            self.child = child

            self.square = square # The size of the square it will wobble within.
            # Include more variables if you'd like to have more control over the positioning.

        def render(self, width, height, st, at):
            if preferences.enable_TXT_Tag == False: 
                return renpy.render(self.child, width, height, st, at)
            # Randomly move the offset of the text's render.
            xoff = (random.random()-.5) * float(self.square)
            yoff = (random.random()-.5) * float(self.square)

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            render.subpixel_blit(child_render, (xoff, yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # Demonstration of using a Transform on the text and applying rotation
    class RotateText(renpy.Displayable):
        def __init__(self, child, speed=300, **kwargs):
            super(RotateText, self).__init__(**kwargs)

            self.child = child

            self.speed = speed # The speed of our rotation

        def render(self, width, height, st, at):
            if preferences.enable_TXT_Tag == False: 
                return renpy.render(self.child, width, height, st, at)
            theta = math.radians(st * float(self.speed))
            t = Transform(child=self.child,  rotate=st*float(self.speed))
            child_render = renpy.render(t, width, height/2, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height/2)

            # Problem with using a Transform though is that each character will be padded
            # Because the rotation may make it wider or taller depending on the character and angle.
            # How best to tackle this though may vary depending on how you'd like to implement it.
            render.blit(child_render, (0,0))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # The following is an alternative version of rotate that allows for rotation in the x and y axis
    # Functionally equivalent to using a Transform and flipping it using ATL xzoom and yzoom constrained between 0 and 1
    # Using a Transform might be better in some cases, but I'll leave this here for anyone who'd prefer to work with angles
    # for this kind of effect.
    # Other matrix functions of note include
    # renpy.display.matrix.perspective(w,h,n,p,f)
    # renpy.display.matrix.screen_projection(w,h) < Renpy space to OpenGL viewport
    # renpy.display.matrix.texture_projection(w,h) < Renpy space to OpenGL render-to-texture
    # You can look up more about them in the renpy\display\matrix_functions.pyx file
    # Credit to the FancyText module creator yukinogatari for the idea.
    # FancyText module can be found at https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=59587
    """
    class RotateText(renpy.Displayable):
        def __init__(self, child, speed=100, **kwargs):
            super(RotateText, self).__init__(**kwargs)

            self.child = child
            self.speed = speed # The speed of our rotation

        def render(self, width, height, st, at):
            angle = st * self.speed
            # Which parameter you put the 'angle' into will affect which axis the render rotates on.
            # Try moving it around and seeing what happens.
            rotation_m = renpy.display.matrix.rotate(angle,0,0)

            child_render = renpy.render(self.child, width, height, st, at)
            c_width, c_height = child_render.get_size()
            # This applies the rotation to our child's render.
            child_render.reverse = rotation_m

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # Math nerds might realize I'm not offsetting the transform.
            # While renpy.display.matrix.offset(x,y,z) is a thing, it won't change much
            # The real place to apply the offset is in your final blit. Which is what we'll calculate here

            # Rotations on x axis
            theta2 = math.radians(st * float(self.speed) + 180)
            c = math.cos(theta2) + 1.0
            xoff = 0
            yoff = c * self.height
            if yoff > self.height:
                yoff = self.height

            render.subpixel_blit(child_render, (xoff,yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]
    """

    # Simple text swap effect
    # It can be prone to having letters out of place when part of a larger string
    # I recommended you pass it the entire line to avoid this issue.
    # Can also just define every line it'll need in advance and just tell it which
    # ones to swap to to be extra sneaky. Then the text won't be in your script at all!
    class SwapText(renpy.Displayable):
        def __init__(self, start_tags, text1, text2, end_tags, swap_time, **kwargs):
            super(SwapText, self).__init__(**kwargs)
            #Style tags we'll need as well as the text
            self.start_tags = start_tags
            self.text1 = text1
            self.text2 = text2
            self.end_tags = end_tags
            # How long between swapping text
            self.s_time = swap_time
            # An internal timer to keep track of when to swap
            self.timer = 0.0
            # Determines if we swap to text1 or text2 next
            self.swap_to_1 = False
            self.child = Text(start_tags + text1 + end_tags)
            self.st = 0.0


        def render(self, width, height, st, at):
            if preferences.enable_TXT_Tag == False: 
                return renpy.render(self.child, width, height, st, at)
            delta = st - self.st # How long since last update
            self.timer += delta
            if self.timer > self.s_time:
                # If time to swap, determine which one to swap to.
                if self.swap_to_1:
                    self.child.set_text(self.start_tags + self.text1 + self.end_tags)
                    self.swap_to_1 = False
                    self.timer = 0.0
                else:
                    self.child.set_text(self.start_tags + self.text2 + self.end_tags)
                    self.swap_to_1 = True
                    self.timer = 0.0

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0,0))
            renpy.redraw(self, 0)

            self.st = st # So we can check how long since last update
            return render

        def visit(self):
            return [ self.child ]

    # An example of text that moves and reacts to the mouse.
    # Sidenote: The position the mouse is distorted if the screen is resized.
    # I did try to find a way to counteract this, but didn't have much luck.
    # Seems to only happen on the x component though. No clue why.
    # If anyone can pinpoint the issue, please let me know and I'll be happy to fix it.
    class MoveText(renpy.Displayable):
        def __init__(self, child, **kwargs):
            super(MoveText, self).__init__(**kwargs)
            self.affect_distance = 150
            self.child = child
            self.mouse_pos = (1000,1000)
            self.pos = (0,0)

        def render(self, width, height, st, at):
            if preferences.enable_TXT_Tag == False: 
                return renpy.render(self.child, width, height, st, at)
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            # x and y we get in the event function are relative to the top left corner of the displayable initially.
            # So we'll want to update it to reflect the actual position of our text
            trans_x = self.mouse_pos[0] - self.pos[0] - (self.width / 2)
            trans_y = self.mouse_pos[1] - self.pos[1] - (self.height / 2)

            vl = math.hypot(trans_x,trans_y)
            xpos, ypos = self.pos
            # Can skip calculation if vector length is further than our specified effect distance
            if vl < self.affect_distance:
                distance = 3.0 * (self.affect_distance-vl) / self.affect_distance
                xpos -= distance * trans_x / vl
                ypos -= distance * trans_y / vl
                self.pos = (xpos, ypos) # Preserve the new pos
            # Use our child's position as determined by the event function
            render.subpixel_blit(child_render, (xpos, ypos))
            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            self.mouse_pos = (x,y)
            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]


    ### CUSTOM TAG FUNCTIONS ###
    # Letters move in a sine wave.
    # Arguments are separated by dashes.
    # Arguments:
    # 'a': (int) The amplitude (height) of the text's sine wave motion. How high and low it'll go from it's default position in pixels.
    # 'p': (float) The period of the wave. Distance between peaks in the wave.
    # 's': (float) The speed of the wave. How fast it moves with time.
    # Example: {bt=[height]}Text{/bt}
    # Example: {bt=h5-p2.0-s0.5}Text{/bt}
    # If a lone number is given, it is treated as the amplitude only to ensure backwards compatibility
    # Example: {bt=10}Text{/bt}

    def name_tag(tag, argument, contents):

        return [
                (renpy.TEXT_TAG, u"color=#64C8FF"),
                (renpy.TEXT_TAG, u"outlinecolor=#004B96"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/outlinecolor"),
                (renpy.TEXT_TAG, u"/color"),
            ]

    def thinking_tag(tag, argument, contents):

        return [
                (renpy.TEXT_TAG, u"color=#AFAFAF".format(color)),
                (renpy.TEXT_TAG, u"outlinecolor=#323232"),
                (renpy.TEXT_TAG, u"i"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/i"),
                (renpy.TEXT_TAG, u"/outlinecolor"),
                (renpy.TEXT_TAG, u"/color"),
            ]

    def bounce_tag(tag, argument, contents):
        new_list = [ ] # The list we will be appending our displayables into
        amp, period, speed = 0, 10.0, 1.0
        if argument == "": # If the argument received is blank, insert a default value
            amp = 4
            period = 10
            speed = 1
        else:
            argument = argument.split('-')
            if len(argument) == 1 and argument[0][0].isdigit(): # Default behavior to ensure backward compatibility
                amp = int(argument[0])
            else:
                for arg in argument:
                    if arg[0] == 'a':
                        amp = int(arg[1:])
                    elif arg[0] == 'p':
                        period = float(arg[1:])
                    elif arg[0] == 's':
                        speed = float(arg[1:])

        char_offset = 0  # Since we want our text to move in a wave,
                         # we want to let each character know where it is in the wave.
                         # So they move in harmony. Otherwise they rise and fall all together.
        my_style = DispTextStyle() # This will keep track of what tags and styling to add to each letter
        my_style.add_tags("b")
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:                                            # Extract every character from the string
                    char_text = Text(my_style.apply_style(char))             # Create a Text displayable with our styles applied
                    char_disp = BounceText(char_text, char_offset, amp=amp, period=period, speed=speed) # Put the Text into the Wrapper
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))     # Add it back in as a displayable
                    char_offset += 1
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = BounceText(my_img, char_offset, amp=amp, period=period, speed=speed)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    char_offset += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            # I honestly never got around to testing this. Not often the text
            # already has a displayable in it. Let me know if it breaks though.
            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(text, char_offset, amp=amp, period=period, speed=speed)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else: # Don't touch any other type of content
                new_list.append((kind,text))

        return new_list

    def laugh_tag(tag, argument, contents):
        new_list = [ ] # The list we will be appending our displayables into
        amp, period, speed = 3, 10.0, 2.0
        if argument == "": # If the argument received is blank, insert a default value
            amp = 5
            period = 10
            speed = 2
        char_offset = 0
        my_style = DispTextStyle() # This will keep track of what tags and styling to add to each letter
        my_style.add_tags("b")
        my_style.add_tags("color=#FFFF96")
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:                                            # Extract every character from the string
                    char_text = Text(my_style.apply_style(char))             # Create a Text displayable with our styles applied
                    char_disp = BounceText(char_text, char_offset, amp=amp, period=period, speed=speed) # Put the Text into the Wrapper
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))     # Add it back in as a displayable
                    char_offset += 1
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = BounceText(my_img, char_offset, amp=amp, period=period, speed=speed)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    char_offset += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            # I honestly never got around to testing this. Not often the text
            # already has a displayable in it. Let me know if it breaks though.
            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(text, char_offset, amp=amp, period=period, speed=speed)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else: # Don't touch any other type of content
                new_list.append((kind,text))

        return new_list

    def giggle_tag(tag, argument, contents):
        new_list = [ ] # The list we will be appending our displayables into
        amp, period, speed = 1, 1, 1
        if argument == "": # If the argument received is blank, insert a default value
            amp = 2
            period = 20
            speed = 1
        char_offset = 0
        my_style = DispTextStyle() # This will keep track of what tags and styling to add to each letter
        my_style.add_tags("color=#FFFF96")
        my_style.add_tags("size=-5")
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:                                            # Extract every character from the string
                    char_text = Text(my_style.apply_style(char))             # Create a Text displayable with our styles applied
                    char_disp = BounceText(char_text, char_offset, amp=amp, period=period, speed=speed) # Put the Text into the Wrapper
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))     # Add it back in as a displayable
                    char_offset += 1
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = BounceText(my_img, char_offset, amp=amp, period=period, speed=speed)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    char_offset += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            # I honestly never got around to testing this. Not often the text
            # already has a displayable in it. Let me know if it breaks though.
            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(text, char_offset, amp=amp, period=period, speed=speed)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else: # Don't touch any other type of content
                new_list.append((kind,text))

        return new_list

    # Letters change position every frame randomly. Good for very angry or quivering dialogue.
    # range: (int) Letters are confined to a square around their default location. Range determines length of the sides of that square.
    #              Higher values will make it very chaotic while smaller values will make it quite minimal.
    # Example: {sc=[range]}Text{/sc}
    def scare_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 1
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = ScareText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = ScareText(my_img, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    def awkward_tag(tag, argument, contents):
        new_list = [ ] # The list we will be appending our displayables into
        amp, period, speed = 1, 1, 1
        if argument == "": # If the argument received is blank, insert a default value
            amp = 2
            period = 25
            speed = 1
        char_offset = 0
        my_style = DispTextStyle() # This will keep track of what tags and styling to add to each letter
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:                                            # Extract every character from the string
                    char_text = Text(my_style.apply_style(char))             # Create a Text displayable with our styles applied
                    char_disp = BounceText(char_text, char_offset, amp=amp, period=period, speed=speed) # Put the Text into the Wrapper
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))     # Add it back in as a displayable
                    char_offset += 1
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = BounceText(my_img, char_offset, amp=amp, period=period, speed=speed)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    char_offset += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            # I honestly never got around to testing this. Not often the text
            # already has a displayable in it. Let me know if it breaks though.
            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(text, char_offset, amp=amp, period=period, speed=speed)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else: # Don't touch any other type of content
                new_list.append((kind,text))

        return new_list

    def panic_tag(tag, argument, contents):
        new_list = [ ] # The list we will be appending our displayables into
        amp, period, speed = 1, 1, 1
        if argument == "": # If the argument received is blank, insert a default value
            amp = 4
            period = 20
            speed = 1
        char_offset = 0
        my_style = DispTextStyle() # This will keep track of what tags and styling to add to each letter
        my_style.add_tags("sc=2")
        my_style.add_tags("size=+10")
        my_style.add_tags("b")
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:                                            # Extract every character from the string
                    char_text = Text(my_style.apply_style(char))             # Create a Text displayable with our styles applied
                    char_disp = BounceText(char_text, char_offset, amp=amp, period=period, speed=speed) # Put the Text into the Wrapper
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))     # Add it back in as a displayable
                    char_offset += 1
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = BounceText(my_img, char_offset, amp=amp, period=period, speed=speed)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    char_offset += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            # I honestly never got around to testing this. Not often the text
            # already has a displayable in it. Let me know if it breaks though.
            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(text, char_offset, amp=amp, period=period, speed=speed)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else: # Don't touch any other type of content
                new_list.append((kind,text))

        return new_list

    # Letters will start off to the right & invisible. And will then move left while increasing their opacity. Good for meditation and calm text.
    # offset: (int) Offset within the line. Needed to help time start of fade-in with other slow text characters.
    # time: (float) How long in seconds the animation lasts.
    # distance: (int) How many pixels the fade in occurs across
    # Example: {fi=[offset]-[time]-[distance]}Text{/fi}
    def fade_in_tag(tag, argument, contents):
        new_list = [ ]
        my_index, fade_time, slide_distance = 0, 5.0, 100
        if argument != "":
            argument = argument.split('-')
            if len(argument) > 0:
                my_index = int(argument[0])
            if len(argument) > 1:
                fade_time = float(argument[1])
            if len(argument) > 2:
                slide_distance = int(argument[2])
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' ')) # Skips blank space since looks weird counting it
                        continue
                    char_text = Text(my_style.apply_style(char))
                    char_disp = FadeInText(char_text, my_index, fade_time, slide_distance)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    my_index += 1
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = FadeInText(my_img, my_index, fade_time, slide_distance)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    my_index += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    def rotate_tag(tag, argument, contents):
        new_list = [ ]
        # Argument here will reprsent the desired speed of the rotation.
        if argument == "":
            argument = 400
        else:
            argument = int(argument)
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = RotateText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = RotateText(my_img, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    # Causes letters to change between two strings every couple of seconds.
    # text1:     (String) First set of characters to display. Should be equal to the length of the characters we're replacing
    # text2:     (String) Second set of characters to display. Should be equal to the length of text1
    # swap_time: (int) Length of time between character swap
    # Arguments are separated by '@'. Length of strings should not exceed length of text they are replacing.
    # Example: {swap=Text@Four@0.5}Text{}
    # This is a pretty static way of doing it mostly made to demonstrate the concept.
    # Included for others to build upon for their needs.
    def swap_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return contents
        text1, _, argument = argument.partition("@")
        text2, _, argument = argument.partition("@")
        if len(text1) != len(text2):
            new_list.append((renpy.TEXT_TEXT, "ERROR!"))
        swap_time = float(argument)

        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                # This one replaces the whole text rather than extracting over letters
                # That way it can take up this whole block with its own Text displayable
                char_disp = SwapText(my_style.start_tags(), text1, text2, my_style.end_tags(), swap_time)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Makes it so the text within moves away from the mouse. More example of what can be done than useful
    # Example: {move}Text{/move}
    def move_tag(tag, argument, contents):
        new_list = [ ]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = MoveText(char_text)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = MoveText(my_img)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Some text effects won't allow for a paragraph break if applied to a whole line
    # Which can cause your text to just continue straight off the screen.
    # To amend this, you can insert the {para} tag.
    # This will let the Text displayable holding us know when to wrap.
    # Can also use \n in most cases. But leaving this for people who may already be using it
    # or for cases where \n doesn't work.
    def paragraph_tag(tag, argument):
        return [(renpy.TEXT_PARAGRAPH, "")]

    """
    # Template tag function to copy off of.
    def TEMPLATE_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 5
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = TEMPLATEText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list
    """

    class ATLText(renpy.Displayable):
        def __init__(self, child, transforms, offset=0, hold=False,**kwargs):
            super(ATLText, self).__init__(**kwargs)
            self.child = At(child, *transforms)
            self.offset = offset
            self.hold = hold
              # If your ATL uses 2+ contains for a character to be used twice, then
              # a fixed is made to contain them. During rendering, this can lead
              # to a render that is far larger than the actual character's render.
              # To combat this, I'm having it check the original Text's render size
              # so we can use that instead. This shouldn't have many consequences,
              # but if you observe something weird, maybe try removing the below and
              # using the child render's size in the render function
            child_render = renpy.render(child, 0, 0, 0, 0)
            self.width, self.height = child_render.get_size()
             # Because of how renpy handles transforms on screens in 7.4.7, we
             # have to update the internals of the transform to get the appropriate
             # time on it. Otherwise our offset won't have the correct effect.
             # If you're using Renpy 7.4.6 or below and this causes issues, you
             # can remove this bit.
            if config.atl_start_on_show:
                renpy.render(self.child, 0, 0, 0, 0)

        def render(self, width, height, st, at):
            # Apply the time offset.
            st = st + self.offset
            at = at + self.offset
            if self.hold:
                st = max(st, 0)
                at = max(at, 0)

            # Get child render and our output render
            child_render = renpy.render(self.child, width, height, st, at)
            # self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # Next section is to figure out the offset applied to the blit
            # Get_Placement returns a tuple containing:
            # xpos, ypos, xanchor, yanchor, xoffset, yoffset, subpixel
            child_pos = self.child.state.get_placement()
            # Sometimes the output of get_placement has some None values in there.
            # So use this to get safe output.
            def none_to_float(param):
                if param is None:
                    return 0.0
                return param
            child_xpos = none_to_float(child_pos[0]) + none_to_float(child_pos[4])
            child_ypos = none_to_float(child_pos[1]) + none_to_float(child_pos[5])

            render.blit(child_render, (child_xpos,child_ypos))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # Allows one to use one or more ATL transforms to define a movement for text.
    # Arguments are separated by ',' and transform parameters are separated by '~'
    # The offset and hold arguments are optional.
    # Arguments:
    #   offset: (float/'#'/'-#') The time offset between two characters (in seconds).
    #                     If #, then it use's the user's cps setting as the offset
    #                     If -#, does the above but treats it as negative.
    #                     See Notes for details on negative offsets
    #   hold: ('#') Tells the displayable to hold the value at 0 if time is negative.
    #               Is ignored if offset is positive.
    #               See Notes on negative offsets for more details.
    #   transform_name: (string) The name of a defined transform.
    #                            Will throw an error if doesn't exist
    #   param: (float/string/'#') A parameter for the transform. Must be ordered by position.
    #     All numbers will be interpreted as floats. Strings should evaluate to a displayable, a global variable OR
    #     optionally, can be left as '#' in order to use the current character as a displayable parameter.
    #     (No current support for keyword args)
    # Notes:
    #   - Transforms are applied using an At() displayable and are added in the same order.
    #
    #   - If a negative offset is supplied, we have to be careful of what time
    #   we supply to the ATL's render function. If we give it a negtive number, it
    #   will treat that value as it's new 0 seconds. So if we feed it -2 seconds
    #   to start, then when it reaches -1.8 seconds, it'll treat that as 0.2 seconds.
    #   This has the effect of syncronizing every letter, which isn't what we want.
    #
    #   - To combat this, if a negative offset is given I instead push the first
    #   letter forward in time. That way each subsequent character can approach
    #   zero with the negative offset.
    #   So, for example, if we have 6 characters and the offset is to be -0.2 seconds,
    #   then the 1st character will start at 1.0 seconds, 2nd will start at 0.8,
    #   and so on until the 6th character starts at 0 seconds.
    #
    #   - However, this may not always be the ideal setup for all transforms,
    #   such as fades. An alternative is then to hold the time at 0 until it becomes
    #   positive. Which is what the 'hold' argument applies.
    #   Re-using the example from before, every character starts at 0 seconds,
    #   The 1st character will start to move immediately, but the 2nd character
    #   will wait 0.2 seconds before starting. The 3rd waits 0.4, 4th waits 0.6,
    #   until the 6th character waits 1.0 seconds before starting.
    #
    # Examples:
    #   {atl=[offset],[hold],[transform_name]~[param]~...),...}Text{/atl}
    #   {atl=0.1, rotate_text~0.5, bounce_text~10}Text{/atl}
    #   {atl=drop_text~#~0.5}Text{/atl}
    #   {atl=-#,#,fade_in_text~1.0~-100}Text{/atl}

    def atl_tag(tag, argument, contents):
        new_list = []
        # Split the argument into a list of transforms and their parameters
        arg_list = argument.split(',')
        atl_list = []
        time_offset = 0
        hold = False
        # Check for an offset
          # See if we want to use the current cps settings
        if arg_list[0] == "#" or arg_list[0] == "-#":
            if preferences.text_cps != 0:
                time_offset = (1.0 / preferences.text_cps)
                if arg_list[0] == "-#":
                    time_offset = time_offset * -1.0
            arg_list.pop(0)
          # Attempt checking if the first parameter is a float.
        else:
            try:
                time_offset = float(arg_list[0])
                arg_list.pop(0)
            except:
                time_offset = 0
        if arg_list[0] == "#":
            hold = True
            arg_list.pop(0)
        # Go through the arguments for transforms.
        # Returns False if it finds a "#" in the params without text set
        # Otherwise returns a list of transforms
        def arg_handler(arg_list, text=None):
            return_list = []
            for arg in arg_list:
                if '~' in arg:
                    txt_param_list = arg.split('~')
                    arg = txt_param_list[0].strip()
                    # Remove the name of the transform from the parameters list
                    txt_param_list.pop(0)
                    param_list = []
                    for i in range(len(txt_param_list)):
                        param = None
                        txt_param_list[i] = txt_param_list[i].strip()
                        # If a #, then we'll have to do some special stuff later
                        if txt_param_list[i] == "#":
                            if text == None: # If we weren't supplied a way to handle this, return
                                return False
                            param_list.append(text)
                            continue
                        # Attempt a float
                        try:
                            param = float(txt_param_list[i])
                        except ValueError:
                            param = None
                        # Attempt a global variable
                        if param == None and txt_param_list[i] in globals():
                            param = globals()[txt_param_list[i]]
                        # Attempt a displayable
                        elif param == None:
                            param = renpy.displayable(txt_param_list[i])
                        param_list.append(param)
                    return_list.append(globals()[arg](*param_list))
                else:
                    arg = arg.strip()
                    return_list.append(globals()[arg])
            return return_list

        # Setup char_index
        char_index = 0
        count_back = False # Used to know if we count forwards or backwards
          # If offset is negative and we aren't holding time at zero, count
          # the number of characters so char_index can count down to 0.
        if time_offset < 0 and not hold:
            for kind,text in contents:
                if kind == renpy.TEXT_TEXT:
                    char_index += len(text)
                # Handles adding images into text. Remove if you don't want this behavior
                elif kind == renpy.TEXT_TAG:
                    if text.find("image") != -1:
                        char_index += 1
            time_offset = time_offset * -1.0
            count_back = True
        atl_list = arg_handler(arg_list) # Attempt to get a list of atl functions
        # Usual kinetic-text-tag text handling
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    if atl_list == False:
                          # If we got a false earlier, then we know we want to call
                          # one of the transforms with the text character as a parameter
                          # so we generate the atl_list necessary for each character.
                        new_atl_list = arg_handler(arg_list, char_text)
                        char_disp = ATLText(char_text, new_atl_list, char_index * time_offset, hold)
                    else:
                        char_disp = ATLText(char_text, atl_list, char_index * time_offset, hold)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    if count_back:
                        char_index -= 1
                    else:
                        char_index += 1
            elif kind == renpy.TEXT_TAG:
                # Handles adding images into text. Remove if you don't want this behavior
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    if atl_list == False:
                        new_atl_list = arg_handler(arg_list, my_img)
                        img_disp = ATLText(my_img, new_atl_list, char_index * time_offset, hold)
                    else:
                        img_disp = ATLText(my_img, atl_list, char_index * time_offset, hold)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    if count_back:
                        char_index -= 1
                    else:
                        char_index += 1
                elif not my_style.add_tags(text):
                        new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list
    
    class ExplodeText(renpy.Displayable):
        def __init__(self, child, timer=2, **kwargs):
            super(ExplodeText, self).__init__(**kwargs)
            self.child = child
            self.curr_x = 0
            self.curr_y = 0
            self.timer = timer
            self.gravity = 300
            self.v0_x = (renpy.random.random() - 0.5) * 800.0
            self.v0_y = renpy.random.random() * -700.0

        def render(self, width, height, st, at):
            curr_x = 0
            curr_y = 0
            if st > self.timer:
                st -= self.timer
                curr_x = self.v0_x * st
                curr_y = self.v0_y * st + self.gravity * pow(st,2)
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # This will position our child's render. Replacing our need for an offset Transform
            render.subpixel_blit(child_render, (curr_x, curr_y))
            if curr_y < 2000:
                renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def visit(self):
            return [ self.child ]

    class ExplodeHalfText(renpy.Displayable):
        def __init__(self, child, length, id, explode_point, timer=2, **kwargs):
            super(ExplodeHalfText, self).__init__(**kwargs)
            self.child = child
            self.curr_x = 0
            self.curr_y = 0
            self.timer = timer
            self.length = length
            self.id = id
            self.gravity = 300
            self.v0_x = (id - explode_point) * 100
            self.v0_y = math.cos((id - explode_point) * math.pi * (1.0/(2.0 * length))) * -900
            # self.v0_y = (-abs(id - explode_point) + length) * -35

        def render(self, width, height, st, at):
            curr_x = 0
            curr_y = 0
            if st > self.timer:
                st -= self.timer
                curr_x = self.v0_x * st
                curr_y = self.v0_y * st + self.gravity * pow(st,2)
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # This will position our child's render. Replacing our need for an offset Transform
            render.subpixel_blit(child_render, (curr_x, curr_y))
            if curr_y < 2000:
                renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def visit(self):
            return [ self.child ]


    # Explodes text out after a certain amount of time
    # timer: (float) How long till the text explodes
    # Example: {explode=[timer]}Text{/explode}
    def explode_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 2
        else:
            argument = float(argument)
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = ExplodeText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = ExplodeText(my_img, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Explodes text out from a point after a certain amount of time
    # center: (int) Position in the string the explosion will be centered on.
    # timer: (float) How long till the text explodes
    # Example: {explode=[center]-[timer]}Text{/explode}
    def explodehalf_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            time_arg = 2
            center_arg = -1
        else:
            center_arg, _, time_arg = argument.partition("-")
            time_arg = float(time_arg)
            center_arg = int(center_arg)
        my_style = DispTextStyle()
        total_length = 0
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                total_length += len(text)
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    curr_id += 1
        curr_id = 0
        if center_arg == -1:
            center_arg = total_length / 2
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = ExplodeHalfText(char_text, total_length, curr_id, center_arg, time_arg)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    curr_id += 1
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = ExplodeHalfText(my_img, total_length, curr_id, center_arg, time_arg)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    curr_id += 1
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list
    
    class GlitchText(renpy.Displayable):
        def __init__(self, child, amount, **kwargs):
            super(GlitchText, self).__init__(**kwargs)
            if isinstance(child, (str, unicode)):
                self.child = Text(child)
            else:
                self.child = child
            self.amount = amount

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            y = 0
            while y < self.height:
                glitch_occurs = renpy.random.random() * 100 < self.amount
                if glitch_occurs:
                    curr_height = renpy.random.randint(-10,10)
                else:
                    curr_height = renpy.random.randint(0,10)
                curr_offset = renpy.random.randint(-10,10)
                curr_surface = child_render.subsurface((0,y,self.width,curr_height))
                if glitch_occurs:
                    render.subpixel_blit(curr_surface, (curr_offset, y))
                else:
                    render.subpixel_blit(curr_surface, (0, y))
                if curr_height > 0:
                    y += curr_height
                else:
                    y -= curr_height
            renpy.redraw(self,0)
            return render

    # Argument is the percertage of the time it'll apply a random offset to a randomly sized slice.
    # offset_percent: (Float between 0.0-100.0) Percentage chance a random block of the render will be offset.
    # 0 will cause it to never occur. 100 will cause an offset on every line.
    # Example: {glitch=59.94}Text{/glitch}
    def glitch_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 10.0
        else:
            argument = float(argument)
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                char_disp = GlitchText(my_style.apply_style(text), argument)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = GlitchText(my_img, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    ##### Made these ones just for fun. Leaving them in here just in case anyone wants
    ##### to use them. Probably will not add them to the Omega tag or to DispTextStyle

    # Takes in two colors, a range and an index and interpolates a new color
    # between the start and end points based on the range and index.
    # color_1: (String of hex color in #rrggbb format) Start of the gradient
    # color_2: (Same as above) End of the gradient
    # range: (int) The number of elements in the gradient
    # id:    (int) The offset into the gradient's range
    # Return: String of interpolated hex color in rrggbb format
    def color_gradient(color_1, color_2, range, index):
        if index == 0:
            return color_1
        if range == index:
            return color_2
        start_col = Color(color_1)
        end_col = Color(color_2)
        return start_col.interpolate(end_col, index * 1.0/range).hexcode

    # Applies a static gradient over text
    # Note: Hex Color = A string giving a hexadecimal color, in the form "#rrggbb".
    # color_1: (Hex Color) The starting color
    # color_2: (Hex Color) The ending color
    # Args are separated by an '-'
    # Example: {gradient=[color_1]-[color_2]}{/gradient}
    def gradient_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return
        else: # Note: all arguments must be supplied
            col_1, _, col_2 = argument.partition('-')
        # Get a count of all the letters we will be applying colors to
        count = 0
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        continue
                    count += 1
        count -= 1
        my_index = 0
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' '))
                        continue
                    new_list.append((renpy.TEXT_TAG, "color=" + color_gradient(col_1, col_2, count, my_index)))
                    new_list.append((renpy.TEXT_TEXT, char))
                    new_list.append((renpy.TEXT_TAG, "/color"))
                    my_index += 1
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # A custom displayable that applies a gradient over a letter of text.
    # Honestly didn't test this works with other text tags since was just for fun
    class GradientText(renpy.Displayable):
        def __init__(self, char, col_list, id, list_end, **kwargs):
            """
            col_list format
                (color_1, color_2, end_id)
            list_end should be the number of gradients in the list
            """
            super(GradientText, self).__init__(**kwargs)

            self.char = char
            self.child = Text(char)
            self.col_list = col_list # Calling it grad_list for gradient might be more appropriate.
            self.id = id
            self.list_end = list_end
            # Figure out which gradient we are in
            for i, element in enumerate(col_list):
                if self.id < element[2]:
                    self.curr_grad = i
                    break
            # Determine the current range (for color_gradient func later)
            if self.curr_grad == 0:
                self.curr_range = self.col_list[0][2]
            else:
                self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]

        def render(self, width, height, st, at):
            if preferences.enable_TXT_Tag == False: 
                return renpy.render(self.child, width, height, st, at)
            my_style = DispTextStyle()
            # Get the color to apply to the text
            if self.curr_grad == 0:
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id))
            else: # color_gradient() expects id to be within the range given. So must reduce to that if exceeding it.
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id - self.col_list[self.curr_grad - 1][2]))

            # Usual retrieval and drawing of child render
            self.child.set_text(my_style.apply_style(self.char))
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            renpy.redraw(self, 0)

            # Iterate id for next render
            self.id += 1
            # If we are at the end of the range update gradient
            if self.id > self.col_list[self.curr_grad][2]:
                self.curr_grad += 1
                # If at the end of our color list, reset back to 0
                if self.curr_grad == self.list_end:
                    self.curr_grad = 0
                    self.id = 0
                    self.curr_range = self.col_list[0][2]
                # Otherwise just update the range
                else:
                    self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]

            return render

        def visit(self):
            return [ self.child ]

    # Applies gradients that smoothly rolls over the letters
    # Argument Notes:
    # Args are seperated by '-'
    # num_of_grad: (int) The number of gradients in the tag. This is to help the function
    #                    know how many gradients it's looking for.
    # The following repeat for the number of gradients specified above
    # grad_col_1: (Hex Color) The starting color of a gradient
    # grad_col_2: (Hex Color) The ending color of a gradient
    # grad_length:      (int) How many values are interpolated in the gradient.
    #                         Can think of this as how many characters the gradient
    #                         spans before the next one starts.
    # Example: {gradient2=[num_of_grad]-[grad_col_1]-[grad_col_2]-[grad_length]-[grad_col_1]-[grad_col_2]-[grad_length]-...} {/gradient2}
    def gradient2_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return
        else: # Note: All arguments must be supplied
            arg_num, _, argument = argument.partition('-') # Number of gradients to read
        arg_num = int(arg_num)
        # Get all arguments
        col_list = []
        end_num = 0
        for i in range(arg_num):
            col_1, _, argument = argument.partition('-')   # Color 1
            col_2, _, argument = argument.partition('-')   # Color 2
            end_num_arg, _, argument = argument.partition('-') # Gradient Length
            end_num += int(end_num_arg) # Converts gradient length into it's ending position
            col_list.append((col_1, col_2, end_num))

        my_index = 0
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' '))
                        continue
                    char_disp = GradientText(my_style.apply_style(char), col_list, my_index, arg_num)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    my_index += 1
                    # Wrap around if reached the end of the gradient list.
                    if my_index >= col_list[arg_num-1][2]:
                        my_index = 0
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list



    # Define our new text tags
    config.custom_text_tags["bt"] = bounce_tag
    config.custom_text_tags["sc"] = scare_tag
    config.custom_text_tags["lg"] = laugh_tag
    config.custom_text_tags["gg"] = giggle_tag
    config.custom_text_tags["nm"] = name_tag
    config.custom_text_tags["aw"] = awkward_tag
    config.custom_text_tags["pa"] = panic_tag
    config.custom_text_tags["fi"] = fade_in_tag
    config.custom_text_tags["swap"] = swap_tag
    config.custom_text_tags["move"] = move_tag
    config.custom_text_tags["mind"] = thinking_tag
    config.custom_text_tags["rotat"] = rotate_tag
    config.self_closing_custom_text_tags["pr"] = paragraph_tag

    # Template tag function
    #config.custom_text_tags[""] = _tag

    config.custom_text_tags["atl"] = atl_tag
    config.custom_text_tags["glitch"] = glitch_tag
    config.custom_text_tags["explode"] = explode_tag
    config.custom_text_tags["gradient"] = gradient_tag
    config.custom_text_tags["gradient2"] = gradient2_tag
    config.custom_text_tags["explodehalf"] = explodehalf_tag

