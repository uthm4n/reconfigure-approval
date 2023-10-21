# reconfigure-approval

At present, it is not possible to schedule a reconfigure task to run on an instance/server in Morpheus. 

To get around this, I have created a Python script that can be run in a Morpheus task and leverage Morpheus' native job capability to schedule the running of a task. 

# Setup:
1. Create an Approve Reconfigure policy (Administration > Policies > Add > Approve Reconfigure)
2. Add the Python script to a Morpheus Task under Library > Automation > Tasks. Add 'requests==2.31.0 jsonpath-ng==1.6.0' to the Additional Packages
3. Create a new Task job under Provisioning > Jobs. Select the task created in the previous step and select a schedule 
