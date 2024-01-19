# Postmortem Report

## Web Stack Debugging Project Outage Resolved

![banner](assets/image.gif)

#### Summary

On January 19th, 2024, at 14:00 East Africa Time (EAT), an outage occurred on a critical server in Nairobi, impacting the web stack of a project. Users attempting to access the project during this period experienced slow response times and intermittent failures, leading to service disruption. Approximately 30% of users relying on the project experienced difficulties.

### Root Cause:
The root cause of the outage was identified as a misconfiguration in the Apache web server settings, specifically in the virtual host configuration. This misconfiguration resulted in unexpected 500 Internal Server Errors and disrupted the normal functioning of the project.

#### Timeline

- **14:00 EAT:** - Issue detected when monitoring tools indicated an increase in server response times and error rates.
- **14:05 EAT:** - Investigation initiated. Checked server logs for any signs of errors or misconfigurations. Identified a recurring 500 Internal Server Error in the Apache logs.
- **14:15 EAT:** - Explored the virtual host configuration and identified the misconfiguration leading to the server errors.
- **14:20 EAT:** - Corrected the virtual host configuration and restarted the Apache web server.
- **14:25 EAT:** - Monitored server logs to ensure the issue was resolved and response times returned to normal.
- **14:40 EAT:** - Confirmed with the team that the project was accessible without errors.

### Misleading Investigation Paths:
![seal](asstes/15jzai.jpg)

Initially explored network-related issues before realizing the problem was specific to the Apache web server configuration.
Considered database performance issues before identifying the Apache misconfiguration as the primary cause.

### Escalation:
The incident was escalated to the DevOps team for collaborative debugging and resolution. The team collaborated in real-time using communication channels to expedite the identification and correction of the issue.

![panik](assets/panik-meme-man-prints.jpg)



#### Resolution:

The issue was resolved by correcting the misconfiguration in the Apache virtual host settings and restarting the Apache web server. Manual testing confirmed that the project was accessible without errors, restoring normal functionality.

![rob](assets/ebcf6c19b336695c91f5c10cf52675d6.jpg)

### Corrective and Preventative Measures:
###Things to Improve/Fix:
- Regular Configuration Audits: Implement periodic audits of web server configurations to identify and rectify potential misconfigurations.
- Automated Monitoring: Enhance monitoring tools to provide immediate alerts for 500 Internal Server Errors or abnormal server responses.

### Tasks to Address the Issue:

Documentation Update: Enhance documentation on web server configuration best practices to educate team members and prevent similar misconfigurations.
Automate Configuration Checks: Implement automated tools to regularly check and validate web server configurations against best practices.

### Conclusion:
The web stack debugging project outage was successfully identified and resolved by addressing a misconfiguration in the Apache virtual host settings. The incident underscores the importance of regular configuration audits and proactive measures to prevent similar disruptions in the future. The implementation of automated tools for configuration validation contributes to maintaining a stable and reliable web stack.





