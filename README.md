# reconfigure-approval

At present, it is not possible to schedule a reconfigure task to run on an instance/server in Morpheus. 

To get around this, I have created a Python script that can be run in a Morpheus task and leverage Morpheus' native job capability to schedule the running of a task. 

# Setup:
1. Create an Approve Reconfigure policy (Administration > Policies > Add > Approve Reconfigure)
2. Add the Python script to a Morpheus Task under Library > Automation > Tasks
3. Navigate to Provisoning > Jobs and create a new job that runs the task 
