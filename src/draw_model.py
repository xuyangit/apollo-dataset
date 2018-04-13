from keras.utils import plot_model
plot_model("../models/steering_model.2381", to_file="smodel.png", show_shapes=True)
plot_model("../models/acc_model.1034", to_file="amodel.png", show_shapes=True)

