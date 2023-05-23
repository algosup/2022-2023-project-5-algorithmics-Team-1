using System;
using Xunit;

namespace Source.Tests
{
    public class LiquidTests
    {
        private const double EPSILON = 0.00000000001;

        [Fact]
        public void TestModSimple()
        {
            // Arrange
            double l1_startlevel = 10;
            Liquid l1 = new Liquid("l1", l1_startlevel);
            double l2_startlevel = 564;
            Liquid l2 = new Liquid("l2", l2_startlevel);

            // Act
            Liquid remaining1 = l1 % 0.5;
            Liquid remaining2 = l2 % 0.3;

            // Assert
            Assert.Equal(l1_startlevel / 2, l1.level);
            Assert.Equal(l1_startlevel / 2, remaining1.level);

            Assert.InRange(l2.level, l2_startlevel * 0.7 - EPSILON, l2_startlevel * 0.7 + EPSILON);
            Assert.InRange(remaining2.level, l2_startlevel * 0.3 - EPSILON, l2_startlevel * 0.3 + EPSILON);
        }

        [Fact]
        public void TestTrueDivSimple()
        {
            // Arrange
            double l1_startlevel = 10;
            Liquid l1 = new Liquid("l1", l1_startlevel);
            double l2_startlevel = 564;
            Liquid l2 = new Liquid("l2", l2_startlevel);

            // Act
            Liquid remaining1 = l1 / 2;
            Liquid remaining2 = l2 / 3;

            // Assert
            Assert.Equal(l1_startlevel / 2, l1.level);
            Assert.Equal(l1_startlevel / 2, remaining1.level);

            Assert.InRange(l2.level, l2_startlevel / 3 - EPSILON, l2_startlevel / 3 + EPSILON);
            Assert.InRange(remaining2.level, l2_startlevel - (l2_startlevel / 3) - EPSILON, l2_startlevel - (l2_startlevel / 3) + EPSILON);
        }
    }
}