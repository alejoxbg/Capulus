#include <string>
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <tf/transform_broadcaster.h>
#include <stdlib.h>
#include <termios.h>
#include <stdio.h>
#include <unistd.h>

char getch()
{
    fd_set set;
    struct timeval timeout;
    int rv;
    char buff = 0;
    int len = 1;
    int filedesc = 0;
    FD_ZERO(&set);
    FD_SET(filedesc, &set);

    timeout.tv_sec = 0;
    timeout.tv_usec = 1000;

    rv = select(filedesc + 1, &set, NULL, NULL, &timeout);

    struct termios old = {0};
    if (tcgetattr(filedesc, &old) < 0)
        ROS_ERROR("tcsetattr()");
    old.c_lflag &= ~ICANON;
    old.c_lflag &= ~ECHO;
    old.c_cc[VMIN] = 1;
    old.c_cc[VTIME] = 0;
    if (tcsetattr(filedesc, TCSANOW, &old) < 0)
        ROS_ERROR("tcsetattr ICANON");

    if(rv == -1)
        ROS_ERROR("select");
    else if(rv == 0)
        ROS_INFO("no_key_pressed");
    else
        read(filedesc, &buff, len );

    old.c_lflag |= ICANON;
    old.c_lflag |= ECHO;
    if (tcsetattr(filedesc, TCSADRAIN, &old) < 0)
        ROS_ERROR ("tcsetattr ~ICANON");
    return (buff);
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "state_publisher");
    ros::NodeHandle n;
    ros::Publisher joint_pub = n.advertise<sensor_msgs::JointState>("joint_states", 1);
    tf::TransformBroadcaster broadcaster;
    ros::Rate loop_rate(30);

    const double degree = M_PI/180;

    // robot state
    double base_wheels_inc= 0.1; 
    double base_wheels= 6.2831; 
    char c;
    double posx=0, posy=0;
    double incx= 0 ,incy=0;

    geometry_msgs::TransformStamped odom_trans;
    sensor_msgs::JointState joint_state;
    odom_trans.header.frame_id = "odom";
    odom_trans.child_frame_id = "base_link";

    while (ros::ok()) {
        //update joint_state
        joint_state.header.stamp = ros::Time::now();
        joint_state.name.resize(4);
        joint_state.position.resize(4);
	joint_state.name[0] ="base_to_wheel1";
        joint_state.position[0] = base_wheels;
	joint_state.name[1] ="base_to_wheel2";
        joint_state.position[1] = base_wheels;
	joint_state.name[2] ="base_to_wheel3";
        joint_state.position[2] = base_wheels;
	joint_state.name[3] ="base_to_wheel4";
        joint_state.position[3] = base_wheels;


                c=getch();
        switch(c)
            {
            case 'w':if(incx>0.02){}else{incx+=0.01;};
            break;
            case'd':if(incy>0.02){}else{incy+=0.01;};
            break;
            case 'a':if(incy<-0.02){}else{incy-=0.01;};
            break;
            case's': if(incx<-0.02){}else{incx-=0.01;};
            break;
            default:;
            }
        
                 if (c == '\x03')
      {
        printf("\n\n                 .     .\n              .  |\\-^-/|  .    \n             /| } O.=.O { |\\\n\n                 CH3EERS\n\n");
        break;
      }

        // update transform
        // (moving in a circle with radius)
        odom_trans.header.stamp = ros::Time::now();
        odom_trans.transform.translation.x = posx;
        odom_trans.transform.translation.y = posy;
        odom_trans.transform.translation.z = 0.0;
        odom_trans.transform.rotation = tf::createQuaternionMsgFromYaw(0);

        //send the joint state and transform
        joint_pub.publish(joint_state);
        broadcaster.sendTransform(odom_trans);


	// Create new robot state
          
          if(incx>0){
          base_wheels -= base_wheels_inc;
          if (base_wheels<0) base_wheels = 6.2831;
		
		  }
          if(incx<0){
          base_wheels += base_wheels_inc;
          if (base_wheels<0) base_wheels = 6.2831;

          }

            c='q';
            posx+=incx;
            posy+=incy;


        // This will adjust as needed per iteration
        loop_rate.sleep();
    }


    return 0;
}
