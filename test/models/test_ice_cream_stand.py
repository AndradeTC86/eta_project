from src.models.ice_cream_stand import IceCreamStand
class TestIceCreamStand:

    def test_flavors_available(self):
        sorveteria = IceCreamStand("Sorveteria", "Tradicional", ["Chocolate", "Morango", "Flocos"])
        expected = '\nNo momento temos os seguintes sabores de sorvete disponíveis:' \
                   '\n\t-Chocolate\n\t-Morango\n\t-Flocos'
        result = sorveteria.flavors_available()
        assert result == expected

    def test_flavors_unavailable(self):
        sorveteria = IceCreamStand("Sorveteria", "Tradicional", [])
        expected = "Estamos sem estoque atualmente!"
        result = sorveteria.flavors_available()
        assert result == expected

    def test_find_flavor(self):
        flavor = 'Flocos'
        sorveteria = IceCreamStand("Sorveteria", "Tradicional", ["Chocolate", "Morango", "Flocos"])
        expected = 'Temos no momento Flocos!'
        result = sorveteria.find_flavor(flavor=flavor)
        assert result == expected

    def test_find_unavailable_flavor(self):
        flavor = 'Flocos'
        sorveteria = IceCreamStand("Sorveteria", "Tradicional", ["Chocolate", "Morango"])
        expected = 'Não temos no momento Flocos!'
        result = sorveteria.find_flavor(flavor=flavor)
        assert result == expected

    def test_find_no_stock_flavor(self):
        flavor = 'Flocos'
        sorveteria = IceCreamStand("Sorveteria", "Tradicional", [])
        expected = 'Estamos sem estoque atualmente!'
        result = sorveteria.find_flavor(flavor=flavor)
        assert result == expected

    def test_find_empty_flavor(self):
        flavor = None
        sorveteria = IceCreamStand("Sorveteria", "Tradicional", ["Chocolate", "Morango"])
        expected = 'Sabor não foi informado'
        result = sorveteria.find_flavor(flavor=flavor)
        assert result == expected

    def test_add_flavor(self):
        flavor = 'Menta'
        sorveteria = IceCreamStand("Sorveteria", "Tradicional", ["Chocolate", "Morango", "Flocos"])
        expected = 'Menta adicionado ao estoque!'
        result = sorveteria.add_flavor(flavor=flavor)
        assert result == expected

    def test_exist_flavor(self):
        flavor = 'Chocolate'
        sorveteria = IceCreamStand("Sorveteria", "Tradicional", ["Chocolate", "Morango", "Flocos"])
        expected = '\nSabor já disponivel!'
        result = sorveteria.add_flavor(flavor=flavor)
        assert result == expected

    def test_empty_flavor(self):
        flavor = None
        sorveteria = IceCreamStand("Sorveteria", "Tradicional", ["Chocolate", "Morango", "Flocos"])
        expected = "Sabor não foi informado"
        result = sorveteria.add_flavor(flavor=flavor)
        assert result == expected
