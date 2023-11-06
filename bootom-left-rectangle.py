import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110
LEFT_MARGIN2=290

arcade.open_window(400, 400, "Complex Loops - Bottom Left Rectangle")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()


for row in range(10):
    for column in range(10 - row):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN
        if row % 2 == 0:
            if column % 2 == 0 :
                arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.WHEAT, tilt_angle=45)
            else:
                arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.SILVER_LAKE_BLUE, tilt_angle=45)
        else:
            if column % 2 == 0 :
                arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.SILVER_LAKE_BLUE, tilt_angle=45)
            else:
                arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.WHEAT, tilt_angle=45)

for row in range(10):
    for column in range(row):
        x = LEFT_MARGIN2 -column * COLUMN_SPACING
        y = row * ROW_SPACING + BOTTOM_MARGIN
        if row % 2 == 0:
            if column % 2 == 0 :
                arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.SILVER_LAKE_BLUE, tilt_angle=45)
            else:
                arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.WHEAT, tilt_angle=45)
        else:
            if column % 2 == 0 :
                arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.WHEAT, tilt_angle=45)
                
            else:
                arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.SILVER_LAKE_BLUE, tilt_angle=45)

arcade.finish_render()
arcade.run()