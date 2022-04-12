# ShittyNN

Aight I will tell you what this is, basically one day I thought to myself, How the fuck does mosquito with its tiny brain
know I am gonna slap it? so the goal of this repo, is to become smarter than a mosquito. From Scratch. And Pain. MAybe use cut some
corners coz you know mosquitoes are dumb??? maybe? who knows how smart they are, basically I will try to tell apart a green tennis ball
or something by the end of this.

I am making the code real shitty, real slow.
I try to come up with as much maths as I can, but I just read up on the hard shit.

## Update

I made a perpceptron I didn't know rosenblatt had an algorithm and ended up making a learning method similar to gradient descent and
rosenblatt's algorithm, it just substracts the delta of the weighted sum from the weights scaled by the reciprocal of the sum of the weights

I named the method reduction since u just reduce the weights till u get a suitable result, but it wasn't very good coz without an activation function some of the datasets wont fit

Then I just implement gradient descent, then i thought, wait why are we substracting dL/dw (L is loss, w is any weight) from the weights
so i just made another thing a gradient of the reciprocal of the slopes since dL/dw didn't make sense to me (honestly i still cant understand the logic) and maned it the correction gradient C = [dw1/dL, dw2/dL, ...]

Then i also made Or logic in the perceptron, but i chose a poor univariate activation function which approached the desired value wery slowly
and also had slope of 0 at x = 2 (i wonder if it is possible to practically stumble on x=2 irl)

Any way for my next thing I will be making a 16*16 perceptron, however i have to build some meaningfull data for this to work
a perceptron wont really detect lines based off of pixel values, i am thinking of doing something like the convulation nueral networks so that
it works a better, or maybe, i could cheat and make a nueral network, the harder choice will be of the activation function so that it can
learn fast.

I also thought of just ditching nueral networks, i realise these things are just so inefficient. kernel machines sound more exciting,
i wanna play around with a nueral network where u keep adding nuerons for each new element in the dataset, kinda like a Modularised nueral
network kernel machine, the researchers at google also wrote something on infinte width deep nueral networks sounds more like a kernel machine
than a nueral network.

## Goals
 - [x] Detect two lists from a dataset of 3 using a perceptron
 - [ ] Detect a line on 16 * 16 using a perceptron
 - [ ] Make a nueral network which identifies vertical and horizontal lines

yah real low standards, I am going through pain dont laugh at my misery here.

## Inspiration

Basically explore efficiency of nueral nets, perceptrons and try and maybe come up with a method for training that i can understand and make
or just copy backpropagation i dunno if i am smart enough, but something simple doing plus and minus here and there should be enough

# Questions

## Why the name?

well, I would tell you to read the code, but i dont want you to get retinal cancer 🥺.

## I have retinal cancer

Too bad, I warned you.

## Can I contribute?
    Yes, but you must explain every single thing you are doing if you know what you are doing to me, I am trynna learn here. pretty pls?

## Your cOdE SuCks.

You think i carE? fuck off

## I might be of help

If you think you can be of **any** help to me, please contact me on discord `WizzyGeek#2356` or https://discord.gg/udmdsFk6Yx
I appericiate any and all kind of support big or small, ranging from typos to just straight up helping me make
the next analog nueral network chip or something i dunno 🤷‍♂️

## When will this work?

Uhhhhhhh, as things are right now, uhh, Never. I think. Probably. Maybe. I dunno.

