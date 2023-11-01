# reconfigure-approval

At present, it is not possible to schedule a [reconfigure](https://docs.morpheusdata.com/en/latest/provisioning/instances/instances.html#performing-instance-actions:~:text=it%20is%20unlocked.-,Reconfigure,-The%20Reconfigure%20action) task to run on an instance/server in [Morpheus](https://morpheusdata.com/). 

To get around this, I have created a script that can run in a Morpheus task. On top of this, you can leverage Morpheus' existing [job capability](https://docs.morpheusdata.com/en/latest/provisioning/jobs/jobs.html) to schedule the running of the task along with an [Approval Reconfigure policy](https://docs.morpheusdata.com/en/latest/administration/policies/policies.html#:~:text=such%20a%20ServiceNow.-,Approve%20Reconfigure,-Sets%20an%20approval). The outcome of this is the acceptance of all Reconfigure tasks pending approval at the time scheduled in the job. 

## **Note: this is a workaround and not a solution to the problem.**

# How it works
1. Retrieves all approvals - https://apidocs.morpheusdata.com/reference/listapprovals
2. Filters through the approvals to only retrieve reconfigures waiting for approval
3. Approves them by using the [Updates a Specific Approval Item](https://apidocs.morpheusdata.com/reference/updateapprovalsitem) API

**Use cases:**
- Accept all reconfigure requests pending approval at a specific time

# Setup:
1. Create an Approve Reconfigure policy (Administration > Policies > Add > Approve Reconfigure)
2. Add the Python script to a Morpheus Task under Library > Automation > Tasks. Add 'requests==2.31.0 jsonpath-ng==1.6.0' into [Additional Packages](https://docs.morpheusdata.com/en/latest/library/automation/automation.html#task-types:~:text=instance.name%20%25%3E-,ADDITIONAL%20PACKAGES%3A,-Additional%20packages%20to)
3. Create a new Task job under Provisioning > Jobs. Select the task created in the previous step and select a schedule 

# Useful links:
- https://docs.morpheusdata.com/en/latest/administration/policies/policies.html
- https://docs.morpheusdata.com/en/latest/provisioning/jobs/jobs.html
- https://docs.morpheusdata.com/en/latest/library/automation/automation.html#tasks
