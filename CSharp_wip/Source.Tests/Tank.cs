using System;
using Xunit;

namespace Source.Tests
{
    public class TankTests
    {
        [Fact]
        public void TestSet()
        {
            // Arrange
            Tank t1 = new Tank("t1", 100, level: 10);

            // Act

            // Assert
            Assert.Equal(10, t1.level);
            Assert.Equal(100, t1.max);
            Assert.Equal("t1", t1.name);
        }

        [Fact]
        public void TestLevel()
        {
            // Arrange
            Tank t1 = new Tank("t1", 100, level: 10);
            Tank t2 = new Tank("t2", 100, level: 20);

            // Act
            t1.MoveUnitTo(t2, 10);

            // Assert
            Assert.Equal(0, t1.level);
            Assert.Equal(30, t2.level);
        }

        [Fact]
        public void TestValidity()
        {
            // Arrange
            List<Tank> tanks = new List<Tank>();
            for (int i = 1; i < 10; i++)
            {
                tanks.Add(new Tank("t" + i, 100, level: i * 10));
            }

            // Act
            // t1 -> t9
            // t2 -> t8
            // t3 -> t7
            // t4 -> t6
            for (int s = 0, e = 8; s < 5; s++, e--)
            {
                tanks[s].MoveUnitTo(tanks[e], tanks[s].level);
            }

            // Assert
            Assert.True(Utils.CheckValidity(tanks, 450));
        }
    }
}