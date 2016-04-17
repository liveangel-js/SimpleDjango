/**
 * Created by liveangel on 15-8-19.
 */
describe('PhoneCat controllers', function() {

  describe('PhoneListCtrl', function(){

    it('should create "phones" model with 3 phones', function() {
      var scope = {},
      ctrl = new PhoneListCtrl(scope);

      expect(scope.phones.length).toBe(3);
    });
  });
});