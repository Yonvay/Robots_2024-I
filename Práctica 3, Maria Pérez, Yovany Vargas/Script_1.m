%%
rosinit;
%%
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist');
velMsg = rosmessage(velPub)
%%
velMsg.Linear.X = 2
velMsg.Linear.Y = 3
send(velPub,velMsg)
pause(1)
%%
rosshutdown;