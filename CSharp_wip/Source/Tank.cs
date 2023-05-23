namespace Source
{
    public class Tank
    {
        public List<Liquid> liquids = new();
        public float max;
        public string name = "t0";

        public double level
        {
            get
            {
                return liquids.Sum(liquid => liquid.level);
            }
        }

        public Tank(string name, float max, float level)
        {
            if (level > max)
            {
                throw new ArgumentException($"Level > Max in Tank {name}.");
            }

            this.name = name;
            this.max = max;
            liquids.Add(new Liquid(name, level));
        }

        public override string ToString()
        {
            return $"{name}({level}/{max})";
        }

        public void MoveUnitTo(Tank target, double level)
        {
            if ((target.max - target.level) < level)
            {
                throw new ArgumentException($"Not enough space available in tank {target} < {level}.");
            }

            if (this.level < level)
            {
                throw new ArgumentException($"Not enough liquid available in tank {this} < {level}.");
            }

            this.MovePercTo(target, level / this.level);
        }

        public void MovePercTo(Tank target, double perc)
        {
            if (target == this)
            {
                return;
            }

            if (this.level * perc > target.max - target.level)
            {
                throw new ArgumentException($"Not enough space available in tank {target} < {perc * 100}% of {this}.");
            }

            if (this.level < this.level * perc)
            {
                throw new ArgumentException($"Not enough liquid available in tank {this} < {perc * 100}% of {target}.");
            }

            foreach (var liquid in this.liquids)
            {
                target.liquids.Add(liquid % perc);
            }
        }
    }
}