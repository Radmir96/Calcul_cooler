class Aluminum_radiator:
    dist_betw_tubes = 9.36
    tube_width = 3.6

    dict_parametrs_MO05 = {'F_cm': 0.6, 'V_cm': 0.0013, 'Num_of_tubes': 11, 'Tube_length': 150,
                           'Heatsink_thickness': 45}
    dict_parametrs_MO1 = {'F_cm': 2.3, 'V_cm': 0.00145, 'Num_of_tubes': 18, 'Tube_length': 200,
                          'Heatsink_thickness': 63}
    dict_parametrs_MO2 = {'F_cm': 4.6, 'V_cm': 0.00165, 'Num_of_tubes': 23, 'Tube_length': 300,
                          'Heatsink_thickness': 63}
    dict_parametrs_MO3 = {'F_cm': 6.7, 'V_cm': 0.0023, 'Num_of_tubes': 34, 'Tube_length': 380, 'Heatsink_thickness': 45}
    dict_parametrs_MO4 = {'F_cm': 10.7, 'V_cm': 0.003, 'Num_of_tubes': 33, 'Tube_length': 470, 'Heatsink_thickness': 63}
    dict_parametrs_MO5 = {'F_cm': 15.2, 'V_cm': 0.003, 'Num_of_tubes': 41, 'Tube_length': 550, 'Heatsink_thickness': 63}
    dict_parametrs_MO6 = {'F_cm': 29.2, 'V_cm': 0.005, 'Num_of_tubes': 41, 'Tube_length': 650, 'Heatsink_thickness': 94}
    dict_parametrs_MO7 = {'F_cm': 35.3, 'V_cm': 0.006, 'Num_of_tubes': 41, 'Tube_length': 800, 'Heatsink_thickness': 94}
    dict_parametrs_MO8 = {'F_cm': 65, 'V_cm': 0.009, 'Num_of_tubes': 48, 'Tube_length': 800, 'Heatsink_thickness': 140}
    dict_parametrs_MO10 = {'F_cm': 36.2, 'V_cm': 0.012, 'Num_of_tubes': 61, 'Tube_length': 550,
                           'Heatsink_thickness': 94}
    dict_parametrs_MO12 = {'F_cm': 58, 'V_cm': 0.0173, 'Num_of_tubes': 82, 'Tube_length': 650, 'Heatsink_thickness': 94}
    dict_parametrs_MO16 = {'F_cm': 130, 'V_cm': 0.038, 'Num_of_tubes': 97, 'Tube_length': 800,
                           'Heatsink_thickness': 140}
    dict_radiators = {'MO05': dict_parametrs_MO05, 'MO1': dict_parametrs_MO1, 'MO2': dict_parametrs_MO2,
                      'MO3': dict_parametrs_MO3, 'MO4': dict_parametrs_MO4, 'MO5': dict_parametrs_MO5,
                      'MO6': dict_parametrs_MO6, 'MO7': dict_parametrs_MO7, 'MO8': dict_parametrs_MO8,
                      'MO10': dict_parametrs_MO10, 'MO12': dict_parametrs_MO12, 'MO16': dict_parametrs_MO16}

    def __init__(self, modul_coller):
        self.name_coller = modul_coller
        self.dict_parametrs = Aluminum_radiator.dict_radiators[modul_coller]
        self.F_cm = self.dict_parametrs['F_cm']
        self.V_cm = self.dict_parametrs['V_cm']
        self.num_of_tubes = self.dict_parametrs['Num_of_tubes']
        self.tube_length = self.dict_parametrs['Tube_length']
        self.heatsink_thickness = self.dict_parametrs['Heatsink_thickness']
        self.f_area_air = None
        self.A_area_oil = None
        self.hydra_diameter = None

    def calcul_f_area_air(self):
        '''Данный метод расчитывает площадь сечения межтрубного пространства для прохождения воздуха'''

        self.f_area_air = self.num_of_tubes * self.tube_length * self.dist_betw_tubes * 0.000001

    def calcul_A_area_oil(self):
        '''Данный метод расчитывает площадь поперечного сечения труб для прохождения масла в радиаторе'''

        self.A_area_oil = self.num_of_tubes * self.heatsink_thickness * self.tube_width * 0.000001

    def calcul_hydra_diameter(self):
        '''Данный метод расчитывает гидравлический диаметр трубки'''

        self.hydra_diameter = 2 * 0.001 * (self.tube_width * self.heatsink_thickness / 3.14) ** (0.5)

    def __str__(self):
        return ' Я радиатор - {},\n площадь рассеивания {}, \n объем радиатора {}, \n {}, ' \
               '\n {}, \n {}'.format(self.name_coller, self.F_cm, self.V_cm, self.f_area_air, self.A_area_oil,
                                     self.hydra_diameter)


class Air_fan_12_or_24:
    dict_parametrs_MO05 = {'Power': 0.8, 'Air_consumption': 0.1528, 'Impeller_speed': 1300}
    dict_parametrs_MO1 = {'Power': 0.8, 'Air_consumption': 0.4723, 'Impeller_speed': 1300}
    dict_parametrs_MO2 = {'Power': 0.8, 'Air_consumption': 0.5, 'Impeller_speed': 1300}
    dict_parametrs_MO3 = {'Power': 0.8, 'Air_consumption': 0.7778, 'Impeller_speed': 1300}
    dict_parametrs_MO4 = {'Power': 0.8, 'Air_consumption': 0.7778, 'Impeller_speed': 1300}
    dict_parametrs_MO5 = {'Power': 0.8, 'Air_consumption': 1, 'Impeller_speed': 1300}
    dict_parametrs_MO6 = {'Power': 0.8, 'Air_consumption': 1.2778, 'Impeller_speed': 1300}
    dict_parametrs_MO10 = {'Power': 0.8, 'Air_consumption': 1.5556, 'Impeller_speed': 1300}
    dict_parametrs_MO6K = {'Power': 0.8, 'Air_consumption': 1.2778, 'Impeller_speed': 1300}

    dict_parameters_fan = {'MO05': dict_parametrs_MO05, 'MO1': dict_parametrs_MO1, 'MO2': dict_parametrs_MO2,
                           'MO3': dict_parametrs_MO3, 'MO4': dict_parametrs_MO4, 'MO5': dict_parametrs_MO5,
                           'MO6': dict_parametrs_MO6, 'MO10': dict_parametrs_MO10, 'MO6K': dict_parametrs_MO6K}

    def __init__(self, modul_coller):
        self.name_fan = modul_coller
        self.dict_parameters = self.dict_parameters_fan[modul_coller]
        self.power = self.dict_parameters['Power']
        self.air_consumption = self.dict_parameters['Air_consumption']
        self.impeller_speed = self.dict_parameters['Impeller_speed']

    def __str__(self):
        return ' Я вентилятор 12/24 - {},\n мощность {}, \n расход воздуха {}, \n скорость вращения {}'.format(
            self.name_fan, self.power, self.air_consumption * 3600, self.impeller_speed)


class AirFan220:

    dict_parametrs_170 = {'Power': 0.032, 'Air_consumption': 0.0828, 'Impeller_speed': 1470}
    dict_parametrs_200 = {'Power': 0.055, 'Air_consumption': 0.2167, 'Impeller_speed': 2500}
    dict_parametrs_250 = {'Power': 0.09, 'Air_consumption': 0.4028, 'Impeller_speed': 2400}
    dict_parametrs_400 = {'Power': 0.18, 'Air_consumption': 1.099, 'Impeller_speed': 1380}
    dict_parametrs_450 = {'Power': 0.37, 'Air_consumption': 1.6361, 'Impeller_speed': 1360}
    dict_parametrs_500 = {'Power': 0.9, 'Air_consumption': 2.67, 'Impeller_speed': 1325}
    dict_parametrs_300 = {'Power': 0.145, 'Air_consumption': 0.6472, 'Impeller_speed': 2300}
    dict_parametrs_350 = {'Power': 0.165, 'Air_consumption': 0.7805, 'Impeller_speed': 1420}
    dict_parametrs_550 = {'Power': 0.55, 'Air_consumption': 2.3638, 'Impeller_speed': 1300}
    dict_parametrs_630 = {'Power': 0.75, 'Air_consumption': 3.1764, 'Impeller_speed': 1360}

    dict_impeller_diam = {'170': dict_parametrs_170, '200': dict_parametrs_200, '250': dict_parametrs_250,
                          '400': dict_parametrs_400,
                          '450': dict_parametrs_450, '500': dict_parametrs_500, '300': dict_parametrs_300,
                          '350': dict_parametrs_350,
                          '550': dict_parametrs_550, '630': dict_parametrs_630}

    def __init__(self, modul_coller=None, requied_air_flow=0, manufacturers='Weiguang'):
        self.name_fan = modul_coller
        self.requied_air_flow = requied_air_flow
        self.manufacturers = manufacturers
        self.dict_parameters = None
        self.power = 0
        self.air_consumption = 0
        self.impeller_speed = 0

    def __str__(self):
        return ' Я вентилятор 220/380 - {},\n мощность {}, \n расход воздуха {}, \n скорость вращения {}'.format(
            self.name_fan, self.power, float(self.air_consumption)*3600, self.impeller_speed)

    def __fan_select_to_flow(self):
        '''Метод выбирает подходящий вентилятор по рекомендуемой производительности, исходя из входных данных объекта'''
        if self.requied_air_flow <= self.dict_parametrs_170['Air_consumption']:
            self.name_fan = 'MO05'
            self.dict_parameters = self.dict_impeller_diam['170']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_170['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_200['Air_consumption']:
            self.name_fan = 'MO1'
            self.dict_parameters = self.dict_impeller_diam['200']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_200['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_250['Air_consumption']:
            self.name_fan = 'MO2'
            self.dict_parameters = self.dict_impeller_diam['250']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_400['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_400['Air_consumption']:
            self.name_fan = 'MO3'
            self.dict_parameters = self.dict_impeller_diam['400']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_400['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_400['Air_consumption']:
            self.name_fan = 'MO4'
            self.dict_parameters = self.dict_impeller_diam['400']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_450['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_450['Air_consumption']:
            self.name_fan = 'MO5'
            self.dict_parameters = self.dict_impeller_diam['450']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_500['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_500['Air_consumption']:
            self.name_fan = 'MO6'
            self.dict_parameters = self.dict_impeller_diam['500']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_550['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_550['Air_consumption']:
            self.name_fan = 'MO7'
            self.dict_parameters = self.dict_impeller_diam['550']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_630['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_630['Air_consumption']:
            self.name_fan = 'MO8'
            self.dict_parameters = self.dict_impeller_diam['630']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_400['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_400['Air_consumption']:
            self.name_fan = 'MO10'
            self.dict_parameters = self.dict_impeller_diam['400']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_500['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_500['Air_consumption']:
            self.name_fan = 'MO12'
            self.dict_parameters = self.dict_impeller_diam['500']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.requied_air_flow > self.dict_parametrs_500['Air_consumption'] and self.requied_air_flow <= self.dict_parametrs_500['Air_consumption']:
            self.name_fan = 'MO16'
            self.dict_parameters = self.dict_impeller_diam['500']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        else:
            print('Вы ввели неккоректное значение расхода воздуха.')

    def __fan_select_to_name(self):
        '''Метод выбирает нужный вентилятор исходя из названия маслоохладителя в серии ООО Аркаим'''
        if self.name_fan == 'MO05':
            self.dict_parameters = self.dict_impeller_diam['170']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO1':
            self.dict_parameters = self.dict_impeller_diam['200']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO2':
            self.dict_parameters = self.dict_impeller_diam['250']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO3':
            self.dict_parameters = self.dict_impeller_diam['400']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO4':
            self.dict_parameters = self.dict_impeller_diam['400']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO5':
            self.dict_parameters = self.dict_impeller_diam['450']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO6':
            self.dict_parameters = self.dict_impeller_diam['500']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO7':
            self.dict_parameters = self.dict_impeller_diam['550']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO8':
            self.dict_parameters = self.dict_impeller_diam['630']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO10':
            self.dict_parameters = self.dict_impeller_diam['400']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO12':
            self.dict_parameters = self.dict_impeller_diam['500']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        elif self.name_fan == 'MO16':
            self.dict_parameters = self.dict_impeller_diam['500']
            self.power = self.dict_parameters['Power']
            self.air_consumption = self.dict_parameters['Air_consumption']
            self.impeller_speed = self.dict_parameters['Impeller_speed']
        else:
            print('Вы ввели неккоректное значение наименования вентилятора')

    def add(self):
        '''Метод контролирует ввод пользователя исходя из ввода вызывает нужные методы выбора'''
        try:
            if self.name_fan is not None:
                self.__fan_select_to_name()
            elif self.requied_air_flow != 0:
                self.__fan_select_to_flow()
            else:
                print('Вы не ввели данные.')
        except:
            print('ОШИБКА: Производительность должна быть допистыимым числом')




class AirFan:

    def __init__(self, modul_coller, fan_voltage=None):
        self.name_culler = modul_coller
        self.fan_voltage = fan_voltage

    def fan_seletion(self):
        pass


class Oil:
    pass


class Air:
    pass


# radiator1 = Aluminum_radiator(modul_coller='MO8')
# print(radiator1)
# fan1 = Air_fan_12_or_24('MO1')
# print(fan1)
fan2 = AirFan220(requied_air_flow=2)
fan2.add()
print(fan2)