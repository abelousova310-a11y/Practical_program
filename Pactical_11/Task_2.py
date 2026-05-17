for bulls in range(0, 11):
    for cows in range(0, 21):
        for calves in range(0, 201):
            if bulls*10 + cows*5 + calves*0.5 == 100:
                print(f"быки={bulls}, коровы={cows}, телята={calves}")