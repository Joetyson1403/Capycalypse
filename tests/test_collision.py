from capycalypse.logic.entity import Entity

def make(x=0, y=0, w=10, h=10):
    return Entity(x, y, w, h)

# AS : Structure méthode Arrange, Act, Assert
def test_rectangles_qui_se_chevauchent():
    # Arrange
    entity1 = make(0, 0, 10, 10)
    entity2 = make(5, 5, 10, 10)
    # Act
    result = entity1.collides(entity2)
    # Assert
    assert result == True

def test_rectangles_eloignes():
    # Arrange
    entity1 = make(0, 0, 10, 10)
    entity2 = make(15, 15, 10, 10)
    # Act
    result = entity1.collides(entity2)
    # Assert
    assert result == False
    
def test_rectangles_qui_se_touchent_juste_au_bord():
    # Arrange
    entity1 = make(0, 0, 10, 10)
    entity2 = make(10, 10, 10, 10)
    # Act
    result = entity1.collides(entity2)
    # Assert
    assert result == False