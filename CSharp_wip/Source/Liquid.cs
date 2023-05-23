namespace Source
{
	public class Liquid
	{
		public string name;
		public double level;

		public Liquid(string name, double level)
		{
			this.name = name;
			this.level = level;
		}

		public override string ToString()
		{
			return $"Liq[{name}:{level}]";
		}

		public static Liquid operator %(Liquid liquid, double perc)
		{
			var source_level = liquid.level;
			liquid.level -= source_level * perc;
			return new Liquid(liquid.name, source_level * perc);
		}

		public static Liquid operator /(Liquid liquid, double num)
		{
			var source_level = liquid.level;
			liquid.level /= num;
			return new Liquid(liquid.name, source_level - liquid.level);
		}
	}
}