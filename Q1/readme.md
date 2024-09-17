Question 1: By default, are Django signals executed synchronously or asynchronously?
Answer: By default, Django signals are executed synchronously. This means that the signal handler (receiver) is executed in the same flow as the code that triggers the signal.

a real-time example for Question 1 regarding the synchronous execution of Django signals, let's consider a practical scenario where we want to send a welcome email to users right after they register on a website.

In this case, we'll use Django's post_save signal to trigger an email-sending function when a new User is created. Since Django signals are executed synchronously by default, the system will wait for the email to be sent before proceeding with the rest of the code.

Scenario: Sending a Welcome Email After User Registration
Explanation:

When a user registers (i.e., when a User object is created), a welcome email is sent via the post_save signal.
The email-sending operation is time-consuming, and since signals are synchronous, the entire process will wait for the email to be sent before proceeding to the next step (e.g., redirecting the user to a different page).
We'll simulate the email-sending process using time.sleep() to mimic the delay in sending an email.