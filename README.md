# Overview
The gorillabot is a bot that I made for [hackNY](https://hackny.org/)'s Slack workspace which sends messages to channels regarding a newsletter I write monthly. I can either send a message at a current time or I can schedule a message after a certain amount of time. 

# All Commands
This is a list of current commands available for use. This list is also a WIP. 

To send a message directly to a specific channel.
``` 
/send <channel_name>
```

To **schedule** a send to a channel. This will send the message at 12 AM EST. 

``` 
/schedule <channel_name> <mm/dd>
```

To list top 10 messages sent or scheduled and the option to delete the messages. 

```
/list
```

To set a deadline. 
```
/deadline <mm/dd>
```

To view deadline.
```
/deadline
```

**Note: Messages can only be posted in specific channels.**