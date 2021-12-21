# Lab 16: Serverless functions

## Instructions to Use

Copy/paste this into the browsers url: https://serverless-chloenott.vercel.app/api/counter_parent?duration_seconds=2

Expected response: An integer representing the final count value. I notice sometimes though it returns 0, so I guess maybe sometimes a cold start takes a bit of time; not certain yet. Seem

## Description

This is a serverless function assignment that assumes vercel is being used to run them. If ran locally, see vercel cli documentation. (Tldr: poetry install, vercel dev).

The api/counter_parent route simply increments a counter by 1 in a loop for the provided duration_seconds, and returns the count value at the end. The purpose was to compare the speed on my local environment versus vercel. It seems vercel runs the count function about 5x slower (3.7E6 counts/s vs 0.7E6 counts/s,). However...

Counter_parent makes a request to counter_child, another serverless function, through an API call which does the actual counting. The plan that I never got around to was to...

Todo: Make asyncronous calls to counter_child from counter_parent. 1000 simultaneous functions are possible for free. The CPU power is proportional to the memory allocated for the function. It would be interesting to allocate the maximum allowed memory per function, and make 1000 asyncronous calls, and sum the returned values. I would expect that count to be substantially higher than my local environment.
