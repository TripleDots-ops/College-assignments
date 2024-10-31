START

    // Step 1: Housekeeping
    DECLARE accountBalance
    DECLARE numberOfOverdrawns
    DECLARE overDrawnFee
    DECLARE fee
    DECLARE newAccountBalance

    // Step 2: Input
    PRINT "Enter the account balance:"
    INPUT accountBalance

    PRINT "Enter the number of times the account was overdrawn:"
    INPUT numberOfOverdrawns

    // Step 3: Process
    IF numberOfOverdrawns > 0 THEN
        fee = (accountBalance * 0.01) - (5 * numberOfOverdrawns)
    ELSE
        fee = 0
    ENDIF

    newAccountBalance = accountBalance - fee

    // Step 4: Output
    PRINT "Calculated Fee: $", fee
    PRINT "New Account Balance: $", newAccountBalance
    PRINT "Thanks for using this program!"

END
