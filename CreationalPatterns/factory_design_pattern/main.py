# module -> file import class
from logistics import RoadLogistics
from dialog import WindowsDialog, LinuxDialog, WebDialog



# Road Logistic - plan delivery
# road_logistic = RoadLogistics()
# road_transcprot = road_logistic.plan_delivery()
# print(road_transcprot.deliver())
#------------------------------------------

# Click and render the windows button
# create_button = WindowsDialog()
# rendering = create_button.render()
# print(rendering.on_click())
# print(rendering.render())


# Click and render the Web button
# create_button = WebDialog()
# rendering = create_button.render()
# print(rendering.on_click())
# print(rendering.render())


# Click and render the linux button
create_button = LinuxDialog()
rendering = create_button.render()
print(rendering.on_click())
print(rendering.render())