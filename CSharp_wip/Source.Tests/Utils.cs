namespace Source.Tests
{
	public class Utils
	{
		public static bool CheckValidity(List<Tank> tanks, double all) {
			return tanks.Sum(t => t.level) == all;
        }
	}
}

