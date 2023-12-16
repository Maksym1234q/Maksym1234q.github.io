from abc import ABC, abstractmethod


class EComAppForHome(ABC):

    def __init__(self, accesses_point, owner):
        self.access_point = accesses_point
        self.owner = owner

    @abstractmethod
    def start_working(self):
        pass

    @abstractmethod
    def stop_working(self):
        pass


class AC(EComAppForHome):
   
    def __init__(self, accesses_point, owner):
        super().__init__(accesses_point, owner)

    def start_working(self):
        return f'{self.owner} started work of AC'

    def stop_working(self):
        return f'{self.owner} stopped work of AC'


class Refrigerator(EComAppForHome):
  
    def __init__(self, accesses_point, owner):
        super().__init__(accesses_point, owner)

    def start_working(self):
        return f'{self.owner} started work of Refrigerator'

    def stop_working(self):
        return f'{self.owner} stopped work of Refrigerator'


class Fan(EComAppForHome):
    
    def __init__(self, accesses_point, owner):
        super().__init__(accesses_point, owner)

    def start_working(self):
        return f'{self.owner} started work of Fan'

    def stop_working(self):
        return f'{self.owner} stopped work of Fan'


class TV(EComAppForHome):
   
    def __init__(self, accesses_point, owner):
        super().__init__(accesses_point, owner)

    def start_working(self):
        return f'{self.owner} started work of TV'

    def stop_working(self):
        return f'{self.owner} stopped work of TV'


class GateOpener(EComAppForHome):
   
    def __init__(self, accesses_point, owner):
        super().__init__(accesses_point, owner)

    def start_working(self):
        return f'{self.owner} started work of Gate Opener'

    def stop_working(self):
        return f'{self.owner} stopped work of Gate Opener'


class Switch:
    
    def __init__(self, e_com_app_for_home: EComAppForHome) -> None:
        self.e_com_app_for_home = e_com_app_for_home

    @abstractmethod
    def turn_on(self):
        return self.e_com_app_for_home.start_working()

    @abstractmethod
    def turn_off(self):
        return self.e_com_app_for_home.stop_working()


class AutomaticRemoteController(Switch):

    def __init__(self, power_capability, usage_place, e_com_app_for_home: EComAppForHome):
        super().__init__(e_com_app_for_home)
        self.power_capability = power_capability
        self.usage_place = usage_place

    def turn_on(self):
        pass

    def turn_off(self):
        pass


class ManualRemoteController(Switch):
    def __init__(self, power_capability, usage_place, max_distance, e_com_app_for_home: EComAppForHome):
        super().__init__(e_com_app_for_home)
        self.power_capability = power_capability
        self.usage_place = usage_place
        self.max_distance = max_distance

    def turn_on(self):
        pass

    def turn_off(self):
        pass


def client_code(switch: Switch):
    print(switch.turn_on())


if __name__ == "__main__":
    e_com_app_for_home = GateOpener(owner='Mr. Robertson', accesses_point='smarthome_point')
    switch = Switch(e_com_app_for_home)
    client_code(switch)

    e_com_app_for_home = TV(owner='Mr. Robertson', accesses_point='smarthome_point')
    switch = Switch(e_com_app_for_home)
    client_code(switch)

    e_com_app_for_home = Refrigerator(owner='Mr. Robertson', accesses_point='smarthome_point')
    switch = Switch(e_com_app_for_home)
    client_code(switch)

