---
layout: post
title:  "Scalable Flaps - Brick Rigs Dev Blog #1"
date:   2024-11-04 09:00:00 +0100
category: brick-rigs
---
Welcome to the first written Brick Rigs development blog post. The goal behind this blog is to show some of the inner workings of Brick Rigs to the people who are interested in the more technical aspects of game development. In this post I will be showing you some of the complexities involved in making flap bricks scalable (they will come in update 1.8).

# Flap Movement

Flaps used to be implemented in a simple way. The moving part was a separate static mesh that was attached to the base mesh. The flap could be moved conveniently by setting its relative rotation.

While this is easy to implement and works perfectly fine, I wanted to optimize it a bit. The problem with needing an additional static mesh component is, that it adds a lot of overhead. There is the sizable memory footprint of a static mesh component, the cost to update the transform of it as well as the rendering overhead. Having the same geometry in a single mesh is generally a lot more performant compared to when it's split into multiple meshes.

Another way to achieve this movement would be to use a skeletal mesh. However, skeletal meshes are a lot less performant than static meshes and would likely be even worse than the two mesh solution. Also, handling skeletal mesh assets in the editor is generally a bit more tedious than static meshes. So that approach was off the table pretty much immediately.

So the perfect solution would be to only need a single static mesh. But as the word 'static' already implies, static meshes cannot deform, or can they...? Well, they can, if you play around with the position of individual vertices in the vertex shader. This sounds more complicated than it really is, because in the Unreal Engine this is a feature in the material editor. You can plug a 3D vector in the 'World Position Offset' pin and move around vertices with it. This is a simple example of using a sine function to move the entire mesh up and down:

![](/assets/scalable-flaps/wpo-sine.gif)

Of course, we don't want to move the entire mesh, just the flap part. A simple and efficient way to do this is to use vertex colors, as it allows us to store per vertex information basically for free. I used the red channel to mask the flap part and the green channel for the hinge part (for now we only need the red channel, the green channel will come in later).

![](/assets/scalable-flaps/vertex-colors.png)

Now I can simply multiply my sine function with the red channel of the vertex color and only the flap will move.

![](/assets/scalable-flaps/wpo-sine-vertex-color.gif)

However, rotating the flap instead of moving it is going to be a bit more complicated. We need to rotate the vertices around the pivot point and rotate vertex normals as well, so the lighting still looks correct. For this Unreal offers a handy little node called 'Rotate About Axis', which can rotate a vector around a pivot point and rotation axis. With two of these nodes we can calculate the new world position offset as well as tangent space normals. To simplify things I created a custom material function called 'Rotate Mesh Around Axis', which takes care of the sometimes confusing math involved and allows me to reuse it on other materials.

![](/assets/scalable-flaps/wpo-rotation.gif)

If we now replace our sine function with a scalar material parameter, we can set the flap to any angle from code.

# Hinge Scaling

Another issue with scalable flaps was going to be the hinge part. The way scalables are implemented, their static mesh is simply proportionally scaled in the X, Y and Z directions. While this works for boxes, wedges, spheres etc., it distorts the hinge of our flap and looks bad.

![](/assets/scalable-flaps/hinge-stretching.gif)

I already knew the solution to this, as it would be very similar to the way it works on scalable wheels. We can use world position offset to customize the position of the hinge vertices and thus apply our own scaling to them. Basically, we want to remove the X scaling on the hinge vertices and apply the Z scaling instead (so the hinge is scaled equally in X and Z direction and thus remains proportional). Here is what that looks like in the material editor:

![](/assets/scalable-flaps/hinge-stretching-fix.png)

With this the hinge will always look correct (as long as the flap isn't scaled up too much along the Z axis, otherwise the hinge becomes bigger than the brick).

![](/assets/scalable-flaps/hinge-stretching-fixed.gif)

# Conclusion

If we now combine our flap rotation system with the hinge scaling fix (and ignore a few other issues and complexities that were involved), we get working scalable flaps.

![](/assets/scalable-flaps/working-flaps.gif)