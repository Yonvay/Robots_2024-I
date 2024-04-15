%%
rosinit;
%%
posPub = rospublisher('/turtle1/pose','turtlesim/Pose');
posMsg = rosmessage(posPub)
%%
posMsg.X = 2;
posMsg.Y = 3;
posMsg.Theta=1.572;
posMsg.LinearVelocity=1;
posMsg.AngularVelocity=1;
send(posPub,posMsg)
pause(1)
%%
rosshutdown;