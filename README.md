# Ex1
Ex1.
Literature review:
a.	the smart elevator
https://www.cs.huji.ac.il/~ai/projects/2014/The_intelevator/files/report.pdf
b.	python-elevator-challenge
https://github.com/mshang/python-elevator-challenge
c.	smart-elevator
https://github.com/satheler/smart-elevator

The mission:
The mission was to get a list of calls for elevator, and for every call to allocate the best elevator so the total time that people are waiting to get to their destination will be the shortest.

The problem:
The problem is that this assignment is to find the best algorithm that allocate an elevator for a call in the best efficiency, but every call list can be different and not like the other list of calls, the advantage that we have in this assignment is that in the beginning of the program we got the list of calls and we are able to analyze the information and not be surprised in the middle of our program, addition, it was very difficult to know were every elevator is, in every second.

The offline algorithm:
The idea of my algorithm is greedy and it works like this:
For every call, check if you have an  available elevator and allocate the fastest elevator, if not, check the direction of the call, if it a call going up, choose the higher elevator thats below the source of the call and is also going up, if you don’t have an elevator like this choose an elevator from the group of elevator going down that are closets to the call destination, if you don’t have an elevator thats going down choose from the group of elevator going up that are closet to the destination, and the same way for call thats are going down.

The algorithm:

For call in call list:

	  If rest_elevator not empty:
		    Choose the fastest;
	  else if the call direction up:
      from up_elevator choose the high elevator below the call;
		else:
        from the down_elevator choose the closet to end;
		else:
        from the up_elevator choose the closet to end;
	  else:
        from down_elevator choose the low elevator above the call;
    else:
        from the up_elevator choose the closet to end;
    else:
        from the down_elevator choose the closet to end;

	  

 


uml:




![uml](https://user-images.githubusercontent.com/93682110/142432380-d5f248f2-318e-48ef-a7f0-cffc04d8ee1e.png)




result:



![WhatsApp Image 2021-11-18 at 16 29 38](https://user-images.githubusercontent.com/93682110/142434447-69167bb5-0ba7-4ca4-9cd6-ad24ca86a99c.jpeg)
