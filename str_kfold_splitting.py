def str_kfold_splitting(x,y,n_splits=10, shuffle=True, random_state =42):

    stratified_kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    performance_results = []
    dict = {}
    k = 1

    for train_index, val_index in stratified_kfold.split(x, y):
        x_train, x_val = x[train_index], x[val_index]
        y_train, y_val = y[train_index], y[val_index]

        del first_model
        first_model = compile(model_1_plus_Droput_aug())
        My_all_callbacks = [Checkpoint(address=f"/content/k_fold/{k}_fold"), My_EarlyStopping_callback]

        history = first_model.fit(
            x=x_train,
            y=y_train,
            validation_data=(x_val, y_val),
            batch_size=batch_size,
            epochs=epochs,
            callbacks=My_all_callbacks).history

        dict[f'{k}_fold'] = np.max(history['val_accuracy'])
        print(f'{k}_fold finished')
        print(f"{k}_fold val_accuracy is:{np.max(history['val_accuracy'])}")
        k += 1
    print(dict)